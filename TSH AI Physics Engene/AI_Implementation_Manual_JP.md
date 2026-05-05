# TSH AI 物理エンジン: 人工知能のための Universal OS
## 実装マニュアル ＆ アーキテクチャ解説 (v1.0)

---

### 0. ファイル構成と役割 (File Inventory)

本プロジェクトを構成する AI 関連ファイルの役割を以下に定義します。

- **tsh_ai_core.py** (微分可能コア)
  - 物理定数を「学習」可能にする PyTorch 実装。
- **tsh_ai_api.py** (宇宙編集 API)
  - AI が物理法則を書き換え、相図を評価するための架け橋。
- **materials.json** (AI 物理辞書)
  - 物理定数（alpha/beta）を AI が読み書きする JSON ファイル。
- **AI_Implementation_Manual_EN.md** (テクニカルマニュアル)
  - 本マニュアルの英語版。
- **AI_Implementation_Manual_JP.md** (テクニカルマニュアル)
  - 本マニュアル（日本語版）。

---

### 1. 概要

TSH AI エンジンは、物理シミュレーションと機械学習を橋渡しする 
3 レイヤー・フレームワークです。これにより、AI は物理状態を **「知覚」** し、
微分可能なエンジンを通じて法則を **「学習」** し、
そして宇宙を **「編集」** することが可能になります。

---

### レイヤー 1：データ構造化（知覚 - Perception）

TSH の状態はテンソルおよび JSON 形式で出力され、
CNN、GNN、Transformer などの AI モデルへシームレスに統合されます。

- **`tsh_ai_core.save_tensors()`**: 
  p-field、チャネルマップ、相図を `.npy` ファイルとして書き出します。
- **`materials.json`**: 
  AI が読み書き可能な「物理法則の辞書」です。
- **`compiler_out.json`**: 
  AI が参照するコンパイラ結果（相転移閾値）。

### レイヤー 2：微分可能エンジン（学習 - Learning）

PyTorch で実装されており、AI による **「物理の逆問題」** の解決を可能にします。

- **自動微分 (Differentiation)**: 
  `loss.backward()` をサポート。`alpha` や `beta` を最適化可能です。
- **応用**: 
  運動からのパラメータ推定、目的の相図を作るための定数探索。

### レイヤー 3：宇宙編集 API（能動性 - Agency）

AI が実行時にシミュレーションの法則を直接書き換えます。

- **`TSHAI_API.edit_material()`**: 
  マテリアル辞書を更新します。
- **フィードバック・ループ**:
  1. AI が新しい `beta`（結合定数）を提案。
  2. `TSHFieldCompiler` が JSON を読み込み、HLSL を再生成。
  3. GPU シミュレーターが新しい物理法則で即座に駆動。

---

### AI 評価指標（目的関数）

AI は以下の指標を用いて「宇宙の質」を評価します。

1. **Core Density**: 終端的な重力崩壊領域の割合。
2. **Structural Entropy**: 相境界の複雑性とトポロジーの豊かさ。
3. **Channel Balance**: チャネルごとの相互作用の分布バランス。

---
*(C) 2026 TSH AI Research Lab. 物理と知能の架け橋。 v1.0*
