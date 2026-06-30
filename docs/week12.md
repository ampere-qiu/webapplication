---
toc: true
---

# Week 12：Paint Chat（Canvas + Socket.IO）

!!! info "このページの目的"
    このページでは、Week 11 で作成したテキストチャットアプリをもとに、Canvas を使ったお絵かき機能を追加する。  
    最終的には、複数のユーザーが同じ画面上でリアルタイムに線を描ける **Paint Chat** を作成する。

    Step 0 では、Week 11 のチャットアプリが正しく動くことを確認する。  
    Step 1 では、React を使わずに HTML と JavaScript だけで Canvas の基本を確認する。  
    Step 2 では、Canvas の処理を React コンポーネント `PaintBoard.js` として作成する。  
    Step 3 では、Socket.IO を使って描画データを他のユーザーと共有する。  
    Step 4 はオプション課題であり、キャンバスのクリア機能とペン色の変更機能を追加する。

---

## ページ内メニュー

- [1. 今回作成するもの](#overview)
- [2. Week 11 と Week 12 の違い](#week11-week12)
- [3. フォルダ構成](#folder)
- [4. Step 0：基本チャットアプリの起動](#step0)
- [5. Step 1：HTML と JavaScript で Canvas を試す](#step1)
- [6. Step 2：PaintBoard.js を作成する](#step2)
- [7. Step 3：Socket.IO で描画をリアルタイム共有する](#step3)
- [8. Step 4：オプション課題](#step4)
- [9. よくあるエラー](#trouble)
- [10. 提出前に：名前と学籍番号を表示する](#student-info)
- [11. 提出方法](#submission)

---

<a id="overview"></a>

## 1. 今回作成するもの

今回作成するものは、**テキストチャット機能にお絵かき機能を追加した Paint Chat アプリ**である。

Week 11 では、ログイン、ユーザー一覧、全体メッセージ、個別メッセージを含むチャットアプリを作成した。Week 12 では、そのアプリに `<canvas>` を追加し、ユーザーがマウスで線を描けるようにする。

| Step | 内容 | 提出対象 |
|---|---|---|
| Step 0 | Week 11 の基本チャットアプリを起動して確認する | 練習用 |
| Step 1 | HTML と JavaScript のみで Canvas の基本を確認する | 練習用 |
| Step 2 | Canvas を React コンポーネント `PaintBoard.js` にする | 練習用 |
| Step 3 | Socket.IO で線の座標を共有し、リアルタイム描画を実現する | 提出対象 |
| Step 4 | クリアボタン、ペン色変更などの機能を追加する | 任意提出 |

!!! important "提出対象"
    提出するのは **Step 3 または Step 4 の完成版のみ** である。  
    Step 0〜Step 2 は練習用である。ただし、Step 3 を理解するために、順番に確認することを推奨する。

---

<a id="week11-week12"></a>

## 2. Week 11 と Week 12 の違い

Week 11 では、Socket.IO を使ってテキストメッセージを送受信した。Week 12 では、テキストではなく、**線を描くための座標データ**を送受信する。

| 項目 | Week 11 | Week 12 |
|---|---|---|
| 主な目的 | テキストチャットを作成する | チャットにお絵かき機能を追加する |
| 送るデータ | メッセージ本文、送信者、宛先 | 線の開始点・終了点、ペン色、クリア命令 |
| 主なイベント | `send_message`, `receive_message` | `draw_line` |
| 追加ファイル | なし | `PaintBoard.js` |
| 使う技術 | React, Express, Socket.IO, Bootstrap | React, Express, Socket.IO, Bootstrap, Canvas API |

!!! note "重要な考え方"
    Week 12 では、Week 11 のコードを最初から作り直すのではない。  
    Week 11 のチャットアプリを土台として、Canvas に関係するコードを追加していく。

---

<a id="folder"></a>

## 3. フォルダ構成

このページでは、次のフォルダ構成を前提とする。

```text
chatapp/
├── .vscode/
│   ├── launch.json
│   ├── tasks.json
│   └── settings.json
├── client/
│   ├── package.json
│   └── src/
│       ├── App.js
│       └── PaintBoard.js
└── server/
    ├── package.json
    └── server.js
```

Week 12 で主に編集するファイルは、次の3つである。

| ファイル | 役割 |
|---|---|
| `client/src/App.js` | チャット画面に `PaintBoard` を表示し、描画データを送受信する |
| `client/src/PaintBoard.js` | Canvas の描画処理を書く React コンポーネント |
| `server/server.js` | `draw_line` イベントを受け取り、全クライアントに中継する |

!!! warning "ファイル名の大文字・小文字"
    `PaintBoard.js` と `paintboard.js` は別のファイル名として扱われることがある。  
    この教材では、ファイル名を **`PaintBoard.js`** とする。

---

---

<a id="step0"></a>

## 4. Step 0：基本チャットアプリの起動

Step 0 では、Week 11 で作成した基本チャットアプリが正しく動作するかを確認する。この段階では、Canvas 機能はまだ含まれない。

### 6.1 Step 0 の目的

Step 0 の目的は、次の3点を確認することである。

- サーバー `server.js` が起動する
- React クライアント `App.js` が起動する
- 複数ユーザーでチャットメッセージを送受信できる

!!! note "なぜ最初に確認するのか"
    Week 12 のお絵かき機能は、Week 11 のチャットアプリの上に追加する。  
    そのため、チャット部分が動いていないと、Canvas のコードを追加しても原因の切り分けが難しくなる。

### 6.2 使用するファイル

Step 0 で使うファイルは次の2つである。

```text
server.js
App.js
```

これらは Moodle+R で配布されている。

### 6.3 動作確認

1. サーバーを起動する。
2. React クライアントを起動する。
3. ブラウザで `http://localhost:3000` を開く。
4. 同じブラウザで複数のタブを開く。
5. それぞれ別のユーザー名でログインする。
6. メッセージが自分と他のユーザーに届くか確認する。
7. ユーザー一覧が正しく更新されるか確認する。

---

<a id="step1"></a>

## 5. Step 1：HTML と JavaScript で Canvas を試す

Step 1 では、React や Socket.IO を使う前に、HTML と JavaScript だけで Canvas の基本を確認する。

### 7.1 Step 1 の目的

Canvas は、HTML5 の描画領域である。JavaScript から命令を出すことで、線、図形、文字などを描くことができる。

Week 12 では、まず Canvas API の基本を理解する。

| メソッド・イベント | 意味 |
|---|---|
| `getContext('2d')` | 2D 描画モードを取得する |
| `beginPath()` | 新しい線を描き始める |
| `moveTo(x, y)` | 線の開始位置を指定する |
| `lineTo(x, y)` | 線の終点を指定する |
| `stroke()` | 線を実際に描画する |
| `clearRect(x, y, w, h)` | 指定範囲を消す |
| `mousedown` | マウスを押したとき |
| `mousemove` | マウスが動いたとき |
| `mouseup` | マウスを離したとき |

---

### 7.2 HTML ファイルを作成する

まず、React フォルダや server フォルダの外に、空の HTML ファイルを作成する。たとえば、プロジェクトの一番上に `canvas_test.html` という名前で保存してもよい。これは実行用のファイルではなく、保存したらブラウザで直接開けばよい。

次に、その HTML ファイルに次のコードを貼り付ける。

```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8" />
  <title>Canvas Drawing</title>
  <style>
    #paintCanvas {
      border: 1px solid gray;
      padding: 0;
      margin: 0;
    }
  </style>
</head>
<body>
  <h2>Canvas Drawing</h2>
  <canvas id="paintCanvas" width="500" height="300"></canvas>

  <script>
    const canvas = document.getElementById('paintCanvas');
    const ctx = canvas.getContext('2d');

    let isDrawing = false;
    let pos = { x: 0, y: 0 };

    function getXY(e) {
      const rect = canvas.getBoundingClientRect();
      const style = getComputedStyle(canvas);

      const borderLeft = parseFloat(style.borderLeftWidth) || 0;
      const borderTop = parseFloat(style.borderTopWidth) || 0;
      const paddingLeft = parseFloat(style.paddingLeft) || 0;
      const paddingTop = parseFloat(style.paddingTop) || 0;

      const scaleX = canvas.width / rect.width;
      const scaleY = canvas.height / rect.height;

      return {
        x: (e.clientX - rect.left - borderLeft - paddingLeft) * scaleX,
        y: (e.clientY - rect.top - borderTop - paddingTop) * scaleY,
      };
    }

    function drawLine(x0, y0, x1, y1, color = '#000') {
      ctx.save();
      ctx.strokeStyle = color;
      ctx.beginPath();
      ctx.moveTo(x0, y0);
      ctx.lineTo(x1, y1);
      ctx.stroke();
      ctx.restore();
    }

    function startDraw(e) {
      isDrawing = true;
      pos = getXY(e);
      document.addEventListener('mousemove', drawOutside);
      document.addEventListener('mouseup', stopDrawOutside);
    }

    function drawOutside(e) {
      if (!isDrawing) return;
      const newPos = getXY(e);
      drawLine(pos.x, pos.y, newPos.x, newPos.y);
      pos = newPos;
    }

    function stopDrawOutside() {
      isDrawing = false;
      document.removeEventListener('mousemove', drawOutside);
      document.removeEventListener('mouseup', stopDrawOutside);
    }

    canvas.addEventListener('mousedown', startDraw);
  </script>
</body>
</html>
```

---

### 7.3 コードの説明

#### HTML 部分

```html
<canvas id="paintCanvas" width="500" height="300"></canvas>
```

これは、幅 500 ピクセル、高さ 300 ピクセルの描画領域を作成している。

---

#### JavaScript 初期化部分

```javascript
const canvas = document.getElementById('paintCanvas');
const ctx = canvas.getContext('2d');
```

`canvas` は HTML の `<canvas>` 要素である。`ctx` は、Canvas に線を描くための 2D 描画コンテキストである。

---

#### 描画状態を保存する変数

```javascript
let isDrawing = false;
let pos = { x: 0, y: 0 };
```

`isDrawing` は、マウスが押されているかどうかを表す。`pos` は、直前のマウス位置を保存する。

---

#### getXY 関数

```javascript
function getXY(e) {
  ...
}
```

ブラウザ上のマウス座標を、Canvas 内部の座標に変換する関数である。

!!! note "なぜ座標変換が必要か"
    マウスの座標はブラウザ画面全体を基準にしている。  
    しかし、線を描くときには Canvas の左上を基準にした座標が必要である。  
    そのため、Canvas の位置、border、padding、拡大縮小を考慮して座標を変換する。

---

#### drawLine 関数

```javascript
function drawLine(x0, y0, x1, y1, color = '#000') {
  ctx.save();
  ctx.strokeStyle = color;
  ctx.beginPath();
  ctx.moveTo(x0, y0);
  ctx.lineTo(x1, y1);
  ctx.stroke();
  ctx.restore();
}
```

この関数は、`(x0, y0)` から `(x1, y1)` まで線を描く。

| コード | 意味 |
|---|---|
| `ctx.save()` | 現在の描画設定を保存する |
| `ctx.strokeStyle = color` | 線の色を設定する |
| `ctx.beginPath()` | 新しい線を描き始める |
| `ctx.moveTo(x0, y0)` | 線の開始点を決める |
| `ctx.lineTo(x1, y1)` | 線の終点を決める |
| `ctx.stroke()` | 線を描画する |
| `ctx.restore()` | 描画設定を元に戻す |

---

### 7.4 Step 1 の確認

次のことを確認する。

- クリック＆ドラッグで線が描ける
- 線がマウスの動きに追従する
- クリックした位置と線の始点がずれない
- キャンバスの外にマウスが出ても描画が続く
- ブラウザの表示倍率を変えても大きくずれない

---

<a id="step2"></a>

## 6. Step 2：PaintBoard.js を作成する

Step 2 では、Step 1 の Canvas 描画処理を React コンポーネントにする。

### 8.1 Step 2 の目的

React アプリの中で Canvas を使うために、`PaintBoard.js` という新しいコンポーネントを作成する。

この段階では、まだ Socket.IO による共有は行わない。自分のブラウザ上で線が描ければよい。

!!! note "React コンポーネントにする理由"
    `PaintBoard.js` として分けることで、Canvas の描画処理を `App.js` から切り離すことができる。  
    これにより、チャット画面のコードと描画処理のコードを分かりやすく管理できる。

---

### 8.2 PaintBoard.js を作成する

`client/src/` の中に、次のファイルを作成する。

```text
PaintBoard.js
```

次のコードを貼り付ける。

```javascript
import React, { useRef, useEffect } from 'react';

const PaintBoard = ({ onDrawLine, penColor = '#000', canvasControlRef }) => {
  const canvasRef = useRef(null);
  const isDrawing = useRef(false);
  const pos = useRef({ x: 0, y: 0 });

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    ctx.lineWidth = 2;
    ctx.strokeStyle = penColor;
  }, [penColor]);

  const getXY = (e) => {
    const canvas = canvasRef.current;
    const rect = canvas.getBoundingClientRect();
    const style = getComputedStyle(canvas);

    const borderLeft = parseFloat(style.borderLeftWidth) || 0;
    const borderTop = parseFloat(style.borderTopWidth) || 0;
    const paddingLeft = parseFloat(style.paddingLeft) || 0;
    const paddingTop = parseFloat(style.paddingTop) || 0;

    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;

    return {
      x: (e.clientX - rect.left - borderLeft - paddingLeft) * scaleX,
      y: (e.clientY - rect.top - borderTop - paddingTop) * scaleY,
    };
  };

  const startDraw = (e) => {
    isDrawing.current = true;
    pos.current = getXY(e);
    document.addEventListener('mousemove', handleDrawOutside);
    document.addEventListener('mouseup', handleStopDrawOutside);
  };

  const draw = (e) => {
    if (!isDrawing.current) return;

    const newPos = getXY(e);
    const ctx = canvasRef.current.getContext('2d');

    ctx.save();
    ctx.strokeStyle = penColor || '#000';
    ctx.beginPath();
    ctx.moveTo(pos.current.x, pos.current.y);
    ctx.lineTo(newPos.x, newPos.y);
    ctx.stroke();
    ctx.restore();

    onDrawLine?.(pos.current.x, pos.current.y, newPos.x, newPos.y);
    pos.current = newPos;
  };

  const stopDraw = () => {
    isDrawing.current = false;
  };

  const handleDrawOutside = (e) => {
    if (isDrawing.current) {
      draw(e);
    }
  };

  const handleStopDrawOutside = () => {
    isDrawing.current = false;
    document.removeEventListener('mousemove', handleDrawOutside);
    document.removeEventListener('mouseup', handleStopDrawOutside);
  };

  useEffect(() => {
    if (!canvasControlRef) return;

    canvasControlRef.current = {
      drawRemoteLine: (x0, y0, x1, y1, remoteColor = '#000') => {
        const ctx = canvasRef.current.getContext('2d');
        ctx.save();
        ctx.strokeStyle = remoteColor;
        ctx.beginPath();
        ctx.moveTo(x0, y0);
        ctx.lineTo(x1, y1);
        ctx.stroke();
        ctx.restore();
      },
      clearCanvas: () => {
        const ctx = canvasRef.current.getContext('2d');
        ctx.clearRect(0, 0, canvasRef.current.width, canvasRef.current.height);
      },
    };
  }, [canvasControlRef]);

  return (
    <canvas
      ref={canvasRef}
      width={500}
      height={300}
      style={{ border: '1px solid gray' }}
      onMouseDown={startDraw}
      onMouseMove={draw}
      onMouseUp={stopDraw}
    />
  );
};

export default PaintBoard;
```

---

### 8.3 App.js で PaintBoard を読み込む

`App.js` の上部に、次を追加する。

```javascript
import PaintBoard from './PaintBoard';
```

---

### 8.4 App.js の画面に PaintBoard を追加する

ログイン後のチャット画面の上部など、好きな場所に次を追加する。

```jsx
<div>
  <PaintBoard />
</div>
```

この時点では、まだ他のユーザーとは共有されない。自分の画面だけで線が描ければ成功である。

!!! note "onDrawLine について"
    `onDrawLine` は、線を描いたときに座標を外へ渡すための関数である。  
    Step 2 では使わなくてもよい。Step 3 で Socket.IO に座標を送るために使う。

---

### 8.5 PaintBoard.js の重要な考え方

#### useRef

`useRef` は、再レンダリングしても値を保持したいときに使う。

| ref | 役割 |
|---|---|
| `canvasRef` | `<canvas>` 要素を参照する |
| `isDrawing` | マウスを押して描画中かどうかを保存する |
| `pos` | 直前のマウス位置を保存する |

---

#### useEffect

```javascript
useEffect(() => {
  const canvas = canvasRef.current;
  const ctx = canvas.getContext('2d');
  ctx.lineCap = 'round';
  ctx.lineJoin = 'round';
  ctx.lineWidth = 2;
  ctx.strokeStyle = penColor;
}, [penColor]);
```

この部分では、Canvas の描画設定を行っている。`penColor` が変更された場合も、線の色を更新できる。

---

#### canvasControlRef

`canvasControlRef` は、`App.js` から `PaintBoard.js` の中の関数を呼び出すために使う。

```javascript
canvasControlRef.current = {
  drawRemoteLine: (...args) => { ... },
  clearCanvas: () => { ... },
};
```

これにより、`App.js` から次のように呼び出せる。

```javascript
paintBoardRef.current.drawRemoteLine(x0, y0, x1, y1, color);
paintBoardRef.current.clearCanvas();
```

---

### 8.6 Step 2 の確認

次のことを確認する。

- React アプリ内に Canvas が表示される
- マウスで線を描ける
- マウスを押していないときは線が描かれない
- `PaintBoard.js` が独立したコンポーネントとして動作する

---

<a id="step3"></a>

## 7. Step 3：Socket.IO で描画をリアルタイム共有する

Step 3 では、Canvas に描いた線を他のユーザーにも表示する。

### 9.1 Step 3 の目的

線を描くとき、Canvas には次のような情報が必要である。

```javascript
{ x0, y0, x1, y1 }
```

これは、線の開始点と終了点を表す。

この座標データを Socket.IO でサーバーに送り、サーバーから他のクライアントへ送ることで、リアルタイム共有を実現する。

```text
自分が線を描く
↓
App.js が draw_line イベントを送る
↓
server.js が draw_line を受け取る
↓
server.js が全クライアントに draw_line を送る
↓
各クライアントが drawRemoteLine() で線を描く
```

---

### 9.2 server.js に draw_line イベントを追加する

`server.js` の `io.on('connection', (socket) => { ... })` の中に、次を追加する。

```javascript
socket.on('draw_line', (data) => {
  io.emit('draw_line', data);
});
```

例：

```javascript
io.on('connection', (socket) => {
  console.log('A user connected:', socket.id);

  socket.on('draw_line', (data) => {
    io.emit('draw_line', data);
  });

  // login, send_message, disconnect などの処理はそのまま残す
});
```

!!! note "io.emit を使う理由"
    `io.emit(...)` は、接続している全員にイベントを送る。  
    これにより、すべてのブラウザに同じ線を表示できる。

---

### 9.3 App.js に paintBoardRef を追加する

`App.js` の state や ref を定義している部分に、次を追加する。

```javascript
const paintBoardRef = useRef(null);
```

`paintBoardRef` は、`App.js` から `PaintBoard.js` の `drawRemoteLine()` を呼び出すために使う。

---

### 9.4 App.js で draw_line を受信する

Socket.IO 接続を作成している `useEffect` の中で、`draw_line` イベントを受け取る。

```javascript
useEffect(() => {
  socketRef.current = io('http://localhost:3001');

  socketRef.current.on('draw_line', (data) => {
    paintBoardRef.current?.drawRemoteLine?.(
      data.x0,
      data.y0,
      data.x1,
      data.y1,
      data.penColor
    );
  });

  return () => {
    socketRef.current.disconnect();
  };
}, []);
```

ここでは、サーバーから受け取った座標を `drawRemoteLine()` に渡している。

!!! note "?. の意味"
    `paintBoardRef.current?.drawRemoteLine?.(...)` の `?.` は、値が存在するときだけ関数を呼び出す書き方である。  
    `paintBoardRef.current` がまだ準備できていない場合でも、エラーになりにくい。

---

### 9.5 PaintBoard を App.js に配置し、描画データを送る

`App.js` の画面表示部分に、次のように `PaintBoard` を配置する。

```jsx
<PaintBoard
  canvasControlRef={paintBoardRef}
  onDrawLine={(x0, y0, x1, y1) => {
    socketRef.current.emit('draw_line', { x0, y0, x1, y1 });
  }}
/>
```

`onDrawLine` は、ユーザーが線を描くたびに呼ばれる。ここで `socketRef.current.emit(...)` を使い、サーバーへ座標データを送る。

---

### 9.6 PaintBoard.js 側の drawRemoteLine

`PaintBoard.js` には、次のような `drawRemoteLine` が必要である。

```javascript
drawRemoteLine: (x0, y0, x1, y1, remoteColor = '#000') => {
  const ctx = canvasRef.current.getContext('2d');
  ctx.save();
  ctx.strokeStyle = remoteColor;
  ctx.beginPath();
  ctx.moveTo(x0, y0);
  ctx.lineTo(x1, y1);
  ctx.stroke();
  ctx.restore();
}
```

この関数は、他のユーザーが描いた線を、自分の Canvas 上に描くための関数である。

---

### 9.7 Step 3 の確認

次のことを確認する。

1. サーバーを再起動する。
2. React クライアントを開く。
3. 2つのタブ、または2つのブラウザで `http://localhost:3000` を開く。
4. それぞれ別のユーザー名でログインする。
5. 一方の画面で線を描く。
6. もう一方の画面にも線が表示されることを確認する。

!!! success "成功条件"
    一方のブラウザで描いた線が、もう一方のブラウザにもリアルタイムで表示されれば成功である。

---

<a id="step4"></a>

## 8. Step 4：オプション課題

Step 4 はオプション課題である。Step 3 までのアプリをもとに、Canvas と Socket.IO の理解を深めるための機能を追加する。

ここでは、次の2つの機能を扱う。

| 課題 | 内容 | 難易度 |
|---|---|---|
| 課題1 | 全体キャンバスを消すボタンを追加する | ★☆☆ |
| 課題2 | ペンの色を選べるようにする | ★★☆ |

---

### 10.1 課題1：全体キャンバスを消すボタンを追加する

#### 目的

キャンバスの下に `Clear Canvas` ボタンを追加し、自分と他のユーザー全員のキャンバスを一括で消せるようにする。

---

#### PaintBoard.js：clearCanvas を定義する

`PaintBoard.js` の `canvasControlRef.current` の中に、次を追加する。

```javascript
clearCanvas: () => {
  const ctx = canvasRef.current.getContext('2d');
  ctx.clearRect(0, 0, canvasRef.current.width, canvasRef.current.height);
}
```

`clearRect(0, 0, width, height)` は、Canvas 全体を消す処理である。

---

#### App.js：Clear Canvas ボタンを追加する

`PaintBoard` の下などに、次のボタンを追加する。

```jsx
<button
  className="btn btn-warning btn-sm"
  onClick={() => {
    // 自分のキャンバスを消去
    paintBoardRef.current?.clearCanvas?.();

    // 他のユーザーにも通知
    socketRef.current.emit('draw_line', { command: 'clearCanvas' });
  }}
>
  Clear Canvas
</button>
```

---

#### App.js：clearCanvas メッセージを受信する

`draw_line` を受信する部分を、次のように変更する。

```javascript
socketRef.current.on('draw_line', (data) => {
  if (data.command === 'clearCanvas') {
    paintBoardRef.current?.clearCanvas?.();
  } else {
    paintBoardRef.current?.drawRemoteLine?.(
      data.x0,
      data.y0,
      data.x1,
      data.y1,
      data.penColor
    );
  }
});
```

`data.command === 'clearCanvas'` の場合は、線を描くのではなく、Canvas 全体を消す。

---

### 10.2 課題2：ペンの色を選べるようにする

#### 目的

ユーザーがペンの色を自由に選べるようにし、その色で線を描けるようにする。また、他のユーザーにも同じ色で表示されるようにする。

---

#### App.js：penColor state を追加する

`App.js` の state を定義している部分に、次を追加する。

```javascript
const [penColor, setPenColor] = useState('#000000');
```

---

#### App.js：カラーピッカーを追加する

`PaintBoard` の上などに、次の UI を追加する。

```jsx
<div className="mb-2">
  <label className="me-2">ペンの色を選ぶ:</label>
  <input
    type="color"
    value={penColor}
    onChange={(e) => setPenColor(e.target.value)}
  />
</div>
```

`type="color"` を使うと、色を選ぶための入力欄を表示できる。

---

#### App.js：PaintBoard に penColor を渡す

`PaintBoard` を次のように変更する。

```jsx
<PaintBoard
  canvasControlRef={paintBoardRef}
  penColor={penColor}
  onDrawLine={(x0, y0, x1, y1) => {
    socketRef.current.emit('draw_line', {
      x0,
      y0,
      x1,
      y1,
      penColor,
    });
  }}
/>
```

`penColor={penColor}` により、自分が描く線の色を `PaintBoard.js` に渡す。  
また、`emit` で `penColor` も送ることで、他のユーザーにも同じ色を伝える。

---

#### PaintBoard.js：penColor を使って描画する

`draw()` 関数の中で、線の色を `penColor` にする。

```javascript
ctx.strokeStyle = penColor || '#000';
```

この行により、自分が選んだ色で線が描かれる。

---

#### PaintBoard.js：リモート描画でも色を使う

`drawRemoteLine()` では、受け取った `remoteColor` を使って線を描く。

```javascript
drawRemoteLine: (x0, y0, x1, y1, remoteColor = '#000') => {
  const ctx = canvasRef.current.getContext('2d');
  ctx.save();
  ctx.strokeStyle = remoteColor;
  ctx.beginPath();
  ctx.moveTo(x0, y0);
  ctx.lineTo(x1, y1);
  ctx.stroke();
  ctx.restore();
}
```

---

### 10.3 Step 4 の確認

次のことを確認する。

- `Clear Canvas` ボタンを押すと、自分の Canvas が消える
- `Clear Canvas` ボタンを押すと、他のユーザーの Canvas も消える
- 色を変更すると、自分の線の色が変わる
- 他のユーザーの画面にも、同じ色で線が表示される

---

<a id="trouble"></a>

## 9. よくあるエラー

### 11.1 `Module not found: Can't resolve './PaintBoard'`

原因：`PaintBoard.js` のファイル名や場所が間違っている。

確認すること：

```text
client/src/PaintBoard.js
```

`App.js` の import は次のようにする。

```javascript
import PaintBoard from './PaintBoard';
```

---

### 11.2 線を描いても他のブラウザに表示されない

確認すること：

- `server.js` に `draw_line` の処理を追加したか
- `server.js` を再起動したか
- `App.js` で `socketRef.current.emit('draw_line', ...)` を書いたか
- `App.js` で `socketRef.current.on('draw_line', ...)` を書いたか
- `PaintBoard` に `canvasControlRef={paintBoardRef}` を渡しているか

---

### 11.3 `paintBoardRef.current` が `null` になる

原因：`PaintBoard` 側で `canvasControlRef.current = {...}` を設定していない可能性がある。

`PaintBoard.js` に次のような `useEffect` があるか確認する。

```javascript
useEffect(() => {
  if (!canvasControlRef) return;

  canvasControlRef.current = {
    drawRemoteLine: (...) => { ... },
    clearCanvas: () => { ... },
  };
}, [canvasControlRef]);
```

---

### 11.4 Clear Canvas が自分だけにしか反映されない

原因：ボタンを押したときに、サーバーへ通知していない可能性がある。

次のコードがあるか確認する。

```javascript
socketRef.current.emit('draw_line', { command: 'clearCanvas' });
```

---

### 11.5 ペンの色が他のユーザーに反映されない

確認すること：

- `penColor` state を作成したか
- `PaintBoard` に `penColor={penColor}` を渡したか
- `emit` するときに `penColor` も送っているか
- `drawRemoteLine()` で `remoteColor` を `ctx.strokeStyle` に設定しているか

---

### 11.6 server.js を変更したのに動きが変わらない

`server.js` を変更した場合は、必ずサーバーを再起動する。

```text
Ctrl + C
node server.js
```

`App.js` や `PaintBoard.js` は保存だけで反映されることが多いが、`server.js` は再起動が必要である。

---

<a id="student-info"></a>

## 10. 提出前に：名前と学籍番号を表示する

提出前に、React アプリの画面上部に自分の名前と学籍番号を表示すること。  
また、提出するスクリーンショットにも、自分の名前と学籍番号が見えるようにすること。

具体的には、チャット画面や PaintBoard の上部に、次のような情報を表示するとよい。

```text
名前: 立命 太郎
学籍番号: 12345678
```

この表示があると、提出物を確認しやすくなる。

---

<a id="submission"></a>

## 11. 提出方法

提出先は Moodle+R である。

提出ファイルは次の3つである。

```text
App.js
server.js
PaintBoard.js
```

提出内容は、**Step 3 または Step 4 の完成版のみ**である。  
また、動作確認した画面のスクリーンショットも提出すること。

| 提出するもの | 説明 |
|---|---|
| `App.js` | Week 11 のチャット画面に PaintBoard を追加した React 側コード |
| `server.js` | `draw_line` イベントを追加したサーバー側コード |
| `PaintBoard.js` | Canvas 描画用の React コンポーネント |
| スクリーンショット | 動作している Paint App の画面を撮影した画像 |

!!! important "提出前チェック"
    提出前に、次のことを確認する。

    - サーバーが起動する
    - React クライアントが起動する
    - 2つのブラウザでログインできる
    - テキストチャットが動く
    - 一方で描いた線が、もう一方にも表示される
    - Step 4 を実装した場合、クリアボタンとペン色変更が動く
    - 画面上部に自分の名前と学籍番号が表示されている
    - 動作している Paint App のスクリーンショットを用意している

