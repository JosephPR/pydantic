"use client";

import { useState, useEffect } from "react";
import { ArrowLeft, Loader2, Sparkles, CheckCircle2 } from "lucide-react";
import { useParams, useRouter } from "next/navigation";

interface Product {
  item_name: string;
  sku: string;
  price: number;
  stock: number;
  image_url: string;
  description: string;
}

export default function ProductPage() {
  const params = useParams();
  const router = useRouter();
  const sku = params.sku as string;
  const [product, setProduct] = useState<Product | null>(null);
  const [loading, setLoading] = useState(true);

  const handleAddToCart = () => {
    if (!product) return;
    try {
      const stored = localStorage.getItem('fast_dantic_cart');
      const currentCart = stored ? JSON.parse(stored) : [];
      const existing = currentCart.find((item: any) => item.sku === product.sku);
      if (existing) {
        existing.quantity += 1;
      } else {
        currentCart.push({ ...product, quantity: 1 });
      }
      localStorage.setItem('fast_dantic_cart', JSON.stringify(currentCart));
      window.dispatchEvent(new Event('cart-updated'));
      router.push('/');
    } catch (e) {
      console.error(e);
      router.push('/');
    }
  };

  useEffect(() => {
    fetch(`http://localhost:8000/products/${sku}`)
      .then((res) => {
        if (!res.ok) throw new Error("Product not found");
        return res.json();
      })
      .then((data) => setProduct(data))
      .catch((err) => console.error(err))
      .finally(() => setLoading(false));
  }, [sku]);

  if (loading) {
    return (
      <div className="min-h-screen bg-zinc-950 flex flex-col items-center justify-center text-zinc-400">
        <Loader2 className="h-8 w-8 animate-spin text-indigo-500 mb-4" />
        <p>Loading architecture details...</p>
      </div>
    );
  }

  if (!product) {
    return (
      <div className="min-h-screen bg-zinc-950 flex flex-col items-center justify-center text-white">
        <h1 className="text-2xl font-bold mb-4">Architecture Not Found</h1>
        <p className="text-zinc-500 mb-8">We could not locate this specific AI agent.</p>
        <button onClick={() => router.back()} className="text-indigo-400 hover:text-indigo-300 flex items-center gap-2 font-medium">
          <ArrowLeft className="w-5 h-5" /> Return to Catalog
        </button>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-zinc-950 text-zinc-50 font-sans selection:bg-indigo-500/30">
      <header className="sticky top-0 z-50 border-b border-zinc-800 bg-zinc-950/80 backdrop-blur-xl">
        <div className="mx-auto flex h-16 max-w-5xl items-center px-6">
          <button onClick={() => router.back()} className="flex items-center gap-2 text-zinc-400 hover:text-white transition-colors font-medium">
            <ArrowLeft className="w-5 h-5" />
            <span>Back to Storefront</span>
          </button>
        </div>
      </header>

      <main className="mx-auto max-w-5xl px-6 py-12 md:py-24">
        <div className="grid gap-12 md:gap-20 md:grid-cols-2 items-start">
          {/* Left Column: Image */}
          <div className="relative aspect-square overflow-hidden rounded-3xl bg-zinc-900 border border-zinc-800 shadow-2xl shadow-indigo-500/5 group">
            <img
              src={product.image_url}
              alt={product.item_name}
              className="h-full w-full object-cover opacity-90 transition-transform duration-700 group-hover:scale-105"
            />
            <div className="absolute inset-0 bg-linear-to-t from-zinc-950/80 via-transparent to-transparent pointer-events-none" />
          </div>

          {/* Right Column: Details */}
          <div className="flex flex-col">
            <div className="mb-6 inline-flex self-start items-center rounded-full border border-indigo-500/30 bg-indigo-500/10 px-4 py-1.5 text-sm font-medium text-indigo-300">
              <Sparkles className="mr-2 h-4 w-4" />
              Enterprise AI Agent
            </div>
            
            <h1 className="mb-4 text-4xl leading-tight md:text-5xl font-bold text-white tracking-tight">{product.item_name}</h1>
            
            <div className="mb-8 flex flex-wrap items-end gap-x-6 gap-y-2">
              <p className="font-mono text-4xl font-medium text-indigo-400">
                ${product.price.toFixed(2)}
              </p>
              <p className="mb-1 text-base text-zinc-500 font-mono">SKU: {product.sku}</p>
            </div>

            <p className="mb-12 text-lg leading-relaxed text-zinc-300 border-l-2 border-zinc-800 pl-6">
              {product.description}
            </p>

            <div className="mb-10 p-6 rounded-2xl bg-zinc-900/50 border border-zinc-800 flex items-center justify-between">
              <div>
                <p className="text-zinc-100 font-medium mb-1">Unlimited Integration License</p>
                <p className="text-sm text-zinc-500">Deploy instantly across your organization</p>
              </div>
              <div className="flex items-center gap-2 text-emerald-400 text-sm font-medium bg-emerald-500/10 px-3 py-1.5 rounded-full border border-emerald-500/20">
                <CheckCircle2 className="w-4 h-4" /> Ready for Deployment
              </div>
            </div>

            <button
              className="flex w-full items-center justify-center rounded-xl bg-indigo-500 px-8 py-4 text-lg font-bold text-white transition-all hover:bg-indigo-600 shadow-lg shadow-indigo-500/20 active:scale-[0.98]"
              onClick={handleAddToCart}
            >
              Add to Cart
            </button>
          </div>
        </div>
      </main>
    </div>
  );
}
