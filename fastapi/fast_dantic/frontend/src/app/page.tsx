"use client";

import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { ShoppingCart, Sparkles, Loader2, Package, CheckCircle2 } from "lucide-react";

// Types matching our backend schemas
interface Product {
  item_name: string;
  sku: string;
  price: number;
  stock: number;
  image_url: string;
}

interface CartItem extends Product {
  quantity: number;
}

const API_URL = "http://localhost:8000";

export default function Storefront() {
  const [products, setProducts] = useState<Product[]>([]);
  const [cart, setCart] = useState<CartItem[]>([]);
  const [isCartOpen, setIsCartOpen] = useState(false);
  
  // AI Order State
  const [magicText, setMagicText] = useState("");
  const [isMagicLoading, setIsMagicLoading] = useState(false);
  
  // Checkout State
  const [isCheckingOut, setIsCheckingOut] = useState(false);
  const [orderSuccess, setOrderSuccess] = useState<string | null>(null);

  // Fetch products on mount
  useEffect(() => {
    fetch(`${API_URL}/products`)
      .then((res) => res.json())
      .then((data) => setProducts(data))
      .catch((err) => console.error("Failed to fetch products:", err));
  }, []);

  const addToCart = (product: Product) => {
    setCart((prev) => {
      const existing = prev.find((item) => item.sku === product.sku);
      if (existing) {
        return prev.map((item) =>
          item.sku === product.sku
            ? { ...item, quantity: item.quantity + 1 }
            : item
        );
      }
      return [...prev, { ...product, quantity: 1 }];
    });
  };

  const removeFromCart = (sku: string) => {
    setCart((prev) => prev.filter((item) => item.sku !== sku));
  };

  const cartTotal = cart.reduce((total, item) => total + item.price * item.quantity, 0);

  const handleManualCheckout = async () => {
    if (cart.length === 0) return;
    setIsCheckingOut(true);
    
    const orderPayload = {
      order_id: Math.floor(Math.random() * 10000), // Random mock ID
      customer_name: "Guest User",
      email: "guest@example.com",
      price: cartTotal,
      is_priority: false,
      items: cart.map(item => ({
        item_name: item.item_name,
        sku: item.sku,
        quantity: item.quantity
      }))
    };

    try {
      const res = await fetch(`${API_URL}/clean-order`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(orderPayload),
      });
      const data = await res.json();
      
      if (data.status === "success") {
        setOrderSuccess(data.message);
        setCart([]);
        setIsCartOpen(false);
        setTimeout(() => setOrderSuccess(null), 5000);
      }
    } catch (err) {
      console.error("Checkout failed:", err);
    } finally {
      setIsCheckingOut(false);
    }
  };

  const handleMagicOrder = async () => {
    if (!magicText.trim()) return;
    setIsMagicLoading(true);
    
    try {
      const res = await fetch(`${API_URL}/extract-order`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ order_text: magicText }),
      });
      const data = await res.json();
      
      // If AI successfully generated the order payload
      if (data && data.items) {
        // We will just process it directly to our clean-order route
        // Wait actually, extract-order returns the structured data directly!
        // So we can say the order was accepted.
        
        // Let's actually push this directly to the fake DB via clean-order to finalize it.
        await fetch(`${API_URL}/clean-order`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(data),
        });

        setOrderSuccess(`AI successfully processed your order! (${data.items.length} items)`);
        setMagicText("");
        setTimeout(() => setOrderSuccess(null), 5000);
      }
    } catch (err) {
      console.error("Magic Order failed:", err);
    } finally {
      setIsMagicLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-zinc-950 text-zinc-50 font-sans selection:bg-indigo-500/30">
      {/* Header */}
      <header className="sticky top-0 z-50 border-b border-zinc-800 bg-zinc-950/80 backdrop-blur-xl">
        <div className="mx-auto flex h-16 max-w-6xl items-center justify-between px-6">
          <div className="flex items-center gap-2 font-bold text-xl tracking-tight">
            <Package className="text-indigo-400" />
            FastDantic Store
          </div>
          <button 
            onClick={() => setIsCartOpen(!isCartOpen)}
            className="relative p-2 text-zinc-400 hover:text-zinc-50 transition-colors"
          >
            <ShoppingCart className="w-6 h-6" />
            {cart.length > 0 && (
              <span className="absolute top-0 right-0 flex h-4 w-4 items-center justify-center rounded-full bg-indigo-500 text-[10px] font-bold text-white">
                {cart.reduce((acc, item) => acc + item.quantity, 0)}
              </span>
            )}
          </button>
        </div>
      </header>

      <main className="mx-auto max-w-6xl px-6 py-12">
        {/* Success Toast */}
        <AnimatePresence>
          {orderSuccess && (
            <motion.div 
              initial={{ opacity: 0, y: -20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              className="mb-8 flex items-center gap-3 rounded-lg border border-emerald-500/20 bg-emerald-500/10 p-4 text-emerald-400"
            >
              <CheckCircle2 className="h-5 w-5" />
              <p className="font-medium">{orderSuccess}</p>
            </motion.div>
          )}
        </AnimatePresence>

        {/* AI Magic Box */}
        <section className="mb-16">
          <div className="relative overflow-hidden rounded-2xl border border-zinc-800 bg-zinc-900/50 p-1">
            <div className="absolute inset-0 bg-gradient-to-r from-indigo-500/10 via-purple-500/10 to-pink-500/10 opacity-50" />
            <div className="relative rounded-xl bg-zinc-950 p-6 sm:p-8">
              <div className="mb-4 flex items-center gap-2">
                <Sparkles className="h-5 w-5 text-indigo-400" />
                <h2 className="text-xl font-semibold">Magic AI Order</h2>
              </div>
              <p className="mb-6 text-zinc-400">
                Don't want to browse? Just tell us what you want and our Pydantic AI agent will handle the rest.
              </p>
              <div className="flex flex-col gap-3 sm:flex-row">
                <input
                  type="text"
                  value={magicText}
                  onChange={(e) => setMagicText(e.target.value)}
                  placeholder="e.g. 'I need a Pro Laptop and two Wireless Mice, no priority shipping'"
                  className="w-full rounded-lg border border-zinc-800 bg-zinc-900 px-4 py-3 placeholder-zinc-500 focus:border-indigo-500 focus:outline-none focus:ring-1 focus:ring-indigo-500 transition-all"
                  onKeyDown={(e) => e.key === 'Enter' && handleMagicOrder()}
                />
                <button
                  onClick={handleMagicOrder}
                  disabled={isMagicLoading || !magicText.trim()}
                  className="flex items-center justify-center whitespace-nowrap rounded-lg bg-indigo-500 px-6 py-3 font-medium text-white transition-all hover:bg-indigo-600 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {isMagicLoading ? <Loader2 className="h-5 w-5 animate-spin" /> : "Process Order"}
                </button>
              </div>
            </div>
          </div>
        </section>

        {/* Products Grid */}
        <section>
          <h2 className="mb-8 text-2xl font-bold">Featured Products</h2>
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {products.map((product) => (
              <motion.div
                key={product.sku}
                whileHover={{ y: -4 }}
                className="group flex flex-col overflow-hidden rounded-xl border border-zinc-800 bg-zinc-900 transition-all hover:border-zinc-700 hover:shadow-2xl hover:shadow-indigo-500/5"
              >
                <div className="aspect-video w-full overflow-hidden bg-zinc-800 relative">
                  {/* We use standard img since the domains aren't configured in next/image */}
                  <img
                    src={product.image_url}
                    alt={product.item_name}
                    className="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105 opacity-80"
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-zinc-900 to-transparent" />
                </div>
                <div className="flex flex-1 flex-col p-6">
                  <div className="mb-2 flex items-start justify-between">
                    <div>
                      <h3 className="font-semibold text-zinc-100">{product.item_name}</h3>
                      <p className="text-sm text-zinc-500">SKU: {product.sku}</p>
                    </div>
                    <span className="font-mono font-medium text-indigo-400">
                      ${product.price.toFixed(2)}
                    </span>
                  </div>
                  <div className="mt-auto pt-6 flex items-center justify-between">
                    <span className="text-sm text-zinc-500">{product.stock} in stock</span>
                    <button
                      onClick={() => addToCart(product)}
                      className="rounded-lg bg-zinc-100 px-4 py-2 text-sm font-medium text-zinc-900 transition-colors hover:bg-white"
                    >
                      Add to Cart
                    </button>
                  </div>
                </div>
              </motion.div>
            ))}
          </div>
        </section>
      </main>

      {/* Slide-over Cart */}
      <AnimatePresence>
        {isCartOpen && (
          <>
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              onClick={() => setIsCartOpen(false)}
              className="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm"
            />
            <motion.div
              initial={{ x: "100%" }}
              animate={{ x: 0 }}
              exit={{ x: "100%" }}
              transition={{ type: "spring", damping: 25, stiffness: 200 }}
              className="fixed inset-y-0 right-0 z-50 flex w-full max-w-md flex-col border-l border-zinc-800 bg-zinc-950 p-6 shadow-2xl"
            >
              <div className="mb-8 flex items-center justify-between">
                <h2 className="text-xl font-bold">Your Cart</h2>
                <button
                  onClick={() => setIsCartOpen(false)}
                  className="text-zinc-500 hover:text-zinc-50"
                >
                  Close
                </button>
              </div>

              {cart.length === 0 ? (
                <div className="flex flex-1 flex-col items-center justify-center text-center text-zinc-500">
                  <ShoppingCart className="mb-4 h-12 w-12 opacity-20" />
                  <p>Your cart is empty.</p>
                </div>
              ) : (
                <>
                  <div className="flex-1 overflow-y-auto pr-2 custom-scrollbar">
                    <ul className="flex flex-col gap-4">
                      {cart.map((item) => (
                        <li key={item.sku} className="flex items-center justify-between rounded-lg border border-zinc-800 bg-zinc-900/50 p-4">
                          <div>
                            <p className="font-medium">{item.item_name}</p>
                            <p className="text-sm text-zinc-500">Qty: {item.quantity}</p>
                          </div>
                          <div className="flex items-center gap-4">
                            <span className="font-medium">${(item.price * item.quantity).toFixed(2)}</span>
                            <button
                              onClick={() => removeFromCart(item.sku)}
                              className="text-xs text-red-400 hover:text-red-300 transition-colors"
                            >
                              Remove
                            </button>
                          </div>
                        </li>
                      ))}
                    </ul>
                  </div>
                  
                  <div className="mt-8 border-t border-zinc-800 pt-6">
                    <div className="mb-6 flex items-center justify-between text-lg font-bold">
                      <span>Total</span>
                      <span>${cartTotal.toFixed(2)}</span>
                    </div>
                    <button
                      onClick={handleManualCheckout}
                      disabled={isCheckingOut}
                      className="flex w-full items-center justify-center rounded-xl bg-indigo-500 py-4 font-bold text-white transition-all hover:bg-indigo-600 disabled:opacity-50 disabled:cursor-not-allowed"
                    >
                      {isCheckingOut ? <Loader2 className="h-5 w-5 animate-spin" /> : "Checkout Now"}
                    </button>
                  </div>
                </>
              )}
            </motion.div>
          </>
        )}
      </AnimatePresence>
    </div>
  );
}
