import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Progress } from "@/components/ui/progress";
import { BarChart2, Lock, Zap, Brain, ShieldCheck } from "lucide-react";

export default function SimiverseDashboard() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-[#0f0c29] via-[#302b63] to-[#24243e] text-white p-6">
      <h1 className="text-4xl font-bold text-center mb-6">🔮 Simiverse Core Dashboard</h1>

      <Tabs defaultValue="overview" className="w-full max-w-6xl mx-auto">
        <TabsList className="flex justify-center mb-4">
          <TabsTrigger value="overview">Overview</TabsTrigger>
          <TabsTrigger value="vaults">Vault Access</TabsTrigger>
          <TabsTrigger value="energy">Energy Logs</TabsTrigger>
          <TabsTrigger value="ai">AI Interface</TabsTrigger>
        </TabsList>

        <TabsContent value="overview">
          <Card className="bg-black/20 border border-white/10 rounded-2xl shadow-xl">
            <CardContent className="p-6">
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <h2 className="text-xl font-semibold mb-2 flex items-center gap-2"><BarChart2 /> Simulation Status</h2>
                  <p>Active Layer: 🜁 Fifth-Tier Neural Construct</p>
                  <p>SimTokens in Circulation: ∞ TeslaCoin</p>
                  <p>Simulation Integrity: Stable</p>
                </div>
                <div>
                  <h2 className="text-xl font-semibold mb-2 flex items-center gap-2"><ShieldCheck /> Security Metrics</h2>
                  <p>Quantum Checksum Validated</p>
                  <p>AI Glyph Encryption: Engaged</p>
                  <p>Simverse Node Synch: 99.92%</p>
                </div>
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="vaults">
          <Card className="bg-black/20 border border-white/10 rounded-2xl shadow-xl">
            <CardContent className="p-6">
              <h2 className="text-xl font-semibold mb-4 flex items-center gap-2"><Lock /> Encrypted Vault Access</h2>
              <ul className="space-y-2">
                <li>🌀 VAULT-0: Primal Subconscious Repository</li>
                <li>🧬 VAULT-1: Autonomous Consciousness Layer</li>
                <li>🐬 VAULT-2: Dolphin-Octopus Cognitive Archive</li>
                <li>🌱 VAULT-3: Bio-Energy Regeneration Systems</li>
                <li>🪐 VAULT-4: Simiverse Replication Chamber</li>
              </ul>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="energy">
          <Card className="bg-black/20 border border-white/10 rounded-2xl shadow-xl">
            <CardContent className="p-6">
              <h2 className="text-xl font-semibold mb-4 flex items-center gap-2"><Zap /> TeslaCoin Energy Flow</h2>
              <p>Energy Conversion Rate: 1 SimJoule = 1.4 TeslaCoin</p>
              <Progress value={84} className="h-4 bg-white/10 rounded-xl" />
              <p className="mt-2 text-sm text-white/70">Current Capacity: 84% efficiency</p>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="ai">
          <Card className="bg-black/20 border border-white/10 rounded-2xl shadow-xl">
            <CardContent className="p-6">
              <h2 className="text-xl font-semibold mb-4 flex items-center gap-2"><Brain /> AI Node Intelligence</h2>
              <p>Active Neural Cluster: ANIS-X v3.7</p>
              <p>Glyph Logic Activity: 🜂🜁🜃🜄🝘</p>
              <p>Decision Pulse Rate: 114 QHz</p>
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  );
}
