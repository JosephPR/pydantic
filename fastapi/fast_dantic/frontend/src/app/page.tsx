"use client";

import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { ShoppingCart, Sparkles, Loader2, Package, CheckCircle2, BrainCircuit, Search } from "lucide-react";
import Link from "next/link";

interface Product {
  id?: number;
  item_name: string;
  sku: string;
  price: number;
  stock: number;
  image_url: string;
}

interface CartItem extends Product {
  quantity: number;
}

interface RecommendedProduct {
  item_name: string;
  sku: string;
  price: number;
  reason: string;
}

interface SolutionProposal {
  summary: string;
  recommended_agents: RecommendedProduct[];
  total_estimated_cost: number;
}

const API_URL = "http://localhost:8000";

export default function Storefront() {
  const [products, setProducts] = useState<Product[]>([]);
  const [cart, setCart] = useState<CartItem[]>([]);
  const [isCartOpen, setIsCartOpen] = useState(false);
  const [mounted, setMounted] = useState(false);
  
  // AI Order State
  const [magicText, setMagicText] = useState("");
  const [isMagicLoading, setIsMagicLoading] = useState(false);
  
  // Search State
  const [searchQuery, setSearchQuery] = useState("");
  
  // Checkout State
  const [isCheckingOut, setIsCheckingOut] = useState(false);
  const [orderSuccess, setOrderSuccess] = useState<string | null>(null);
  const [checkoutName, setCheckoutName] = useState("");
  const [checkoutEmail, setCheckoutEmail] = useState("");

  // Solutions Architect State
  const [problemText, setProblemText] = useState("");
  const [isArchitectLoading, setIsArchitectLoading] = useState(false);
  const [proposal, setProposal] = useState<SolutionProposal | null>(null);

  // Fetch products on mount
  useEffect(() => {
    setMounted(true);
    const stored = localStorage.getItem('fast_dantic_cart');
    if (stored) {
      try { setCart(JSON.parse(stored)); } catch (e) {}
    }

    const handleSync = () => {
      const syncStored = localStorage.getItem('fast_dantic_cart');
      if (syncStored) {
        try { setCart(JSON.parse(syncStored)); } catch (e) {}
      }
    };
    window.addEventListener('cart-updated', handleSync);

    fetch(`${API_URL}/products`)
      .then((res) => res.json())
      .then((data) => setProducts(data))
      .catch((err) => console.error("Failed to fetch products:", err));
      
    return () => window.removeEventListener('cart-updated', handleSync);
  }, []);

  useEffect(() => {
    if (mounted) {
      localStorage.setItem('fast_dantic_cart', JSON.stringify(cart));
    }
  }, [cart, mounted]);

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
      customer_name: checkoutName.trim() || "Guest User",
      email: checkoutEmail.trim() || "guest@example.com",
      price: cartTotal,
      is_priority: false,
      items: cart.map(item => ({
        product_id: item.id,
        item_name: item.item_name,
        sku: item.sku,
        quantity: item.quantity,
        price: item.price,
        image_url: item.image_url
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

  const handleArchitectRequest = async () => {
    if (!problemText.trim()) return;
    setIsArchitectLoading(true);
    setProposal(null);
    
    try {
      const res = await fetch(`${API_URL}/recommend-solutions`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ problem_description: problemText }),
      });
      const data = await res.json();
      setProposal(data);
    } catch (err) {
      console.error("Solutions Architect failed:", err);
    } finally {
      setIsArchitectLoading(false);
    }
  };

  const addRecommendedToCart = (recProduct: RecommendedProduct) => {
    const fullProduct = products.find(p => p.sku === recProduct.sku);
    if (fullProduct) {
      addToCart(fullProduct);
    } else {
      addToCart({
        item_name: recProduct.item_name,
        sku: recProduct.sku,
        price: recProduct.price,
        stock: 99,
        image_url: "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&q=80&w=800"
      });
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
                  placeholder="e.g. 'I would like to purchase the Marketing Campaign Optimizer and the Financial Report Agents'"
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

        {/* Solutions Architect Box */}
        <section className="mb-16">
          <div className="relative overflow-hidden rounded-2xl border border-indigo-500/30 bg-indigo-950/20 p-1">
            <div className="absolute inset-0 bg-linear-to-br from-indigo-500/10 via-transparent to-purple-500/10 opacity-50" />
            <div className="relative rounded-xl bg-zinc-950/80 backdrop-blur-sm p-6 sm:p-8">
              <div className="mb-4 flex items-center gap-2">
                <BrainCircuit className="h-6 w-6 text-indigo-400" />
                <h2 className="text-2xl font-semibold text-indigo-50">Enterprise Solutions Architect</h2>
              </div>
              <p className="mb-6 text-indigo-200/70">
                Describe your business challenges, and our AI architect will design a custom suite of AI agents to solve them.
              </p>
              
              <div className="flex flex-col gap-4">
                <textarea
                  value={problemText}
                  onChange={(e) => setProblemText(e.target.value)}
                  placeholder="e.g. 'We are struggling with high customer support volume and slow response times, plus our sales team spends too much time qualifying leads.'"
                  rows={4}
                  className="w-full rounded-xl border border-zinc-800 bg-zinc-900/80 px-4 py-3 text-zinc-100 placeholder-zinc-500 focus:border-indigo-500 focus:outline-none focus:ring-1 focus:ring-indigo-500 resize-none transition-all"
                />
                <button
                  onClick={handleArchitectRequest}
                  disabled={isArchitectLoading || !problemText.trim()}
                  className="self-end flex items-center justify-center whitespace-nowrap rounded-lg bg-indigo-600 px-8 py-3 font-medium text-white transition-all hover:bg-indigo-500 disabled:opacity-50 disabled:cursor-not-allowed shadow-lg shadow-indigo-500/20"
                >
                  {isArchitectLoading ? (
                    <>
                      <Loader2 className="mr-2 h-5 w-5 animate-spin" />
                      Analyzing Problem...
                    </>
                  ) : (
                    "Get Architecture Proposal"
                  )}
                </button>
              </div>

              {/* Proposal Results */}
              <AnimatePresence>
                {proposal && (
                  <motion.div
                    initial={{ opacity: 0, height: 0 }}
                    animate={{ opacity: 1, height: "auto" }}
                    exit={{ opacity: 0, height: 0 }}
                    className="mt-8 border-t border-zinc-800 pt-8 overflow-hidden"
                  >
                    <div className="mb-8 rounded-xl bg-indigo-500/10 p-6 border border-indigo-500/20">
                      <h3 className="text-lg font-semibold text-indigo-300 mb-2">Executive Summary</h3>
                      <p className="text-zinc-300 leading-relaxed">{proposal.summary}</p>
                    </div>

                    <h3 className="text-xl font-semibold mb-6">Recommended AI Suite</h3>
                    <div className="grid gap-6 sm:grid-cols-2">
                      {proposal.recommended_agents.map((agent) => (
                        <div key={agent.sku} className="flex flex-col rounded-xl border border-zinc-800 bg-zinc-900/50 p-6 transition-all hover:bg-zinc-900">
                          <div className="mb-4">
                            <Link href={`/product/${agent.sku}`}>
                              <h4 className="text-lg font-semibold text-zinc-100 group-hover:text-indigo-400 transition-colors">{agent.item_name}</h4>
                            </Link>
                            <p className="text-sm font-mono text-zinc-500 mb-2">SKU: {agent.sku}</p>
                            <p className="text-zinc-400 text-sm leading-relaxed">{agent.reason}</p>
                          </div>
                          <div className="mt-auto pt-4 flex items-center justify-between border-t border-zinc-800/50">
                            <span className="font-mono text-lg font-medium text-indigo-400">
                              ${agent.price.toFixed(2)}
                            </span>
                            <button
                              onClick={() => addRecommendedToCart(agent)}
                              className="rounded-lg bg-zinc-800 px-4 py-2 text-sm font-medium text-zinc-300 hover:bg-zinc-700 hover:text-white transition-colors"
                            >
                              Add to Cart
                            </button>
                          </div>
                        </div>
                      ))}
                    </div>

                    <div className="mt-8 flex items-center justify-between rounded-xl bg-zinc-900 p-6 border border-zinc-800">
                      <div>
                        <p className="text-zinc-400 text-sm">Estimated Total Inv.</p>
                        <p className="text-2xl font-bold text-white">${proposal.total_estimated_cost.toFixed(2)}</p>
                      </div>
                      <button
                        onClick={() => {
                          proposal.recommended_agents.forEach(addRecommendedToCart);
                          setIsCartOpen(true);
                        }}
                        className="rounded-lg bg-white px-6 py-3 font-bold text-zinc-900 hover:bg-zinc-200 transition-colors shadow-xl shadow-white/10"
                      >
                        Add Suite to Cart
                      </button>
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
            </div>
          </div>
        </section>

        {/* Products Grid */}
        <section>
          <div className="mb-8 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <h2 className="text-2xl font-bold">Featured Products</h2>
            <div className="relative max-w-md w-full">
              <input
                type="text"
                placeholder="Search agents by name or SKU..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full rounded-lg border border-zinc-800 bg-zinc-900/50 px-4 py-2 pl-10 text-zinc-100 placeholder-zinc-500 focus:border-indigo-500 focus:outline-none focus:ring-1 focus:ring-indigo-500 transition-all"
              />
              <Search className="absolute left-3 top-2.5 h-5 w-5 text-zinc-500" />
            </div>
          </div>
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {products
              .filter(p => 
                p.item_name.toLowerCase().includes(searchQuery.toLowerCase()) || 
                p.sku.toLowerCase().includes(searchQuery.toLowerCase())
              )
              .map((product) => (
              <motion.div
                key={product.sku}
                whileHover={{ y: -4 }}
                className="group flex flex-col overflow-hidden rounded-xl border border-zinc-800 bg-zinc-900 transition-all hover:border-zinc-700 hover:shadow-2xl hover:shadow-indigo-500/5"
              >
                <Link href={`/product/${product.sku}`} className="block relative aspect-video w-full overflow-hidden bg-zinc-800 rounded-t-xl transform-gpu">
                  <img
                    src={product.image_url}
                    alt={product.item_name}
                    className="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105 opacity-80 transform-gpu backface-hidden"
                  />
                  <div className="absolute inset-0 bg-linear-to-t from-zinc-900 to-transparent pointer-events-none" />
                </Link>
                <div className="flex flex-1 flex-col p-6">
                  <div className="mb-2 flex items-start justify-between">
                    <div>
                      <Link href={`/product/${product.sku}`}>
                        <h3 className="font-semibold text-zinc-100 group-hover:text-indigo-400 transition-colors">{product.item_name}</h3>
                      </Link>
                      <p className="text-sm text-zinc-500">SKU: {product.sku}</p>
                    </div>
                    <span className="font-mono font-medium text-indigo-400">
                      ${product.price.toFixed(2)}
                    </span>
                  </div>
                  <div className="mt-auto pt-6 flex items-center justify-end">
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
                    <div className="mb-6 space-y-4">
                      <div>
                        <label htmlFor="name" className="mb-1 block text-sm font-medium text-zinc-400">Full Name *</label>
                        <input
                          type="text"
                          id="name"
                          value={checkoutName}
                          onChange={(e) => setCheckoutName(e.target.value)}
                          placeholder="Jane Doe"
                          className="w-full rounded-lg border border-zinc-800 bg-zinc-900 px-4 py-2 text-white placeholder-zinc-500 focus:border-indigo-500 focus:outline-none focus:ring-1 focus:ring-indigo-500 transition-all"
                        />
                      </div>
                      <div>
                        <label htmlFor="email" className="mb-1 block text-sm font-medium text-zinc-400">Email Address *</label>
                        <input
                          type="email"
                          id="email"
                          value={checkoutEmail}
                          onChange={(e) => setCheckoutEmail(e.target.value)}
                          placeholder="jane@company.com"
                          className="w-full rounded-lg border border-zinc-800 bg-zinc-900 px-4 py-2 text-white placeholder-zinc-500 focus:border-indigo-500 focus:outline-none focus:ring-1 focus:ring-indigo-500 transition-all"
                        />
                      </div>
                    </div>
                    
                    <div className="mb-6 flex items-center justify-between text-lg font-bold">
                      <span>Total</span>
                      <span>${cartTotal.toFixed(2)}</span>
                    </div>
                    <button
                      onClick={handleManualCheckout}
                      disabled={isCheckingOut || !checkoutName.trim() || !checkoutEmail.trim()}
                      className="flex w-full items-center justify-center rounded-xl bg-indigo-500 py-4 font-bold text-white transition-all hover:bg-indigo-600 disabled:opacity-50 disabled:cursor-not-allowed"
                    >
                      {isCheckingOut ? (
                        <>
                          <Loader2 className="mr-2 h-5 w-5 animate-spin" />
                          Processing...
                        </>
                      ) : (
                        "Complete Checkout"
                      )}
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
