---
toc: true
---

# Week 11：チャット機能（テキストチャット）＋ Bootstrap スタイリング

!!! info "このページの目的"
    このページでは、Socket.IO を使ったチャットアプリを段階的に拡張する。

    Step 0 では、Bootstrap を使わないプレーンなチャットアプリを実行する。  
    Step 1 以降では、前の Step から「追加するコード」または「変更するコード」だけを確認しながら進める。

---

## ページ内メニュー

- [1. 今回作成するもの](#overview)
- [2. なぜ Step 0 のコードを配布するのか](#why-step0)
- [3. フォルダ構成](#folder)
- [4. VS Code ランチャーの準備](#vscode)
- [5. 手動で実行する方法](#run)
- [6. Step 0：プレーンなチャットアプリを実行する](#step0)
- [7. Step 1：Bootstrap で画面をスタイリングする](#step1)
- [8. Step 2：ログイン機能を追加する](#step2)
- [9. Step 3：接続中ユーザー一覧を表示する](#step3)
- [10. Step 4：特定ユーザーへのメッセージ送信を追加する](#step4)
- [11. Step 5：チャレンジ・任意](#step5)
- [12. よくあるエラー](#trouble)
- [13. 提出前に：名前と学籍番号を画面上部に表示する](#student-info)
- [14. 提出方法](#submission)

---

<a id="overview"></a>

## 1. 今回作成するもの

今回作成するものは、Socket.IO を使ったテキストチャットアプリである。

最初は、全員にメッセージを送るだけのシンプルなチャットである。  
その後、次の機能を順番に追加する。

| Step | 内容 |
|---|---|
| Step 0 | Bootstrap を使わないプレーンなチャットアプリを実行する |
| Step 1 | Bootstrap を使って画面を整える |
| Step 2 | ログイン機能を追加する |
| Step 3 | 現在接続中のユーザー一覧を表示する |
| Step 4 | 特定ユーザーにだけメッセージを送信できるようにする |
| Step 5 | 任意の追加機能を実装する |

!!! note "このページの使い方"
    Step 0 では、`App.js` と `server.js` の全体コードを示す。  
    Step 1 以降では、前の Step から追加・変更する部分だけを示す。  
    そのため、必ず Step 0 → Step 1 → Step 2 → Step 3 → Step 4 の順番で進めること。

!!! tip "ハイライトの見方"
    Step 1 以降のコードでは、**新しく追加する部分**または**前の Step から変更された部分**をハイライトしている。  
    例えば Step 1 では、Bootstrap に関係する `className` や `style` の行だけをハイライトしている。

!!! note "再現方法"
    このページは、Step 0 の全体コードから始め、Step 1〜Step 4 の変更を順番に追加すると、授業用の最終コードを再現できる構成である。  
    途中の Step を飛ばすと、必要な state や event listener が不足するため、必ず順番に進めること。

---

<a id="why-step0"></a>

## 2. なぜ Step 0 のコードを配布するのか

Week 10 では、React、Node.js、Express、Socket.IO を使って、基本的なチャットアプリを一から作成した。

Week 11 では、同じ内容をもう一度最初から作るのではなく、**チャット機能を拡張すること**に集中する。  
そのため、Step 0 では、すでに動くプレーンなチャットアプリのコードを配布する。

---

### 2.1 Week 10 と Week 11 の違い

| 項目 | Week 10 | Week 11 |
|---|---|---|
| 主な目的 | Socket.IO の基本を理解する | チャットアプリを拡張する |
| 作るもの | シンプルなリアルタイムチャット | ログイン、ユーザー一覧、個別メッセージ付きチャット |
| 進め方 | 基本コードを一から作る | Step 0 の配布コードをもとに機能を追加する |
| メッセージ | 全員に送るだけ | 全員または特定ユーザーに送る |
| ユーザー管理 | ほとんど行わない | ユーザー名と socket.id をサーバーで管理する |

---

### 2.2 Step 0 の役割

Step 0 のコードは、Week 11 の出発点である。

Step 0 では、次のことだけを確認する。

- React クライアントが起動する
- Express + Socket.IO サーバーが起動する
- クライアントとサーバーが接続できる
- メッセージを送受信できる

つまり、Step 0 は「完成形」ではない。  
Step 1 以降で、少しずつ機能を追加するための土台である。

---

### 2.3 なぜ最初から全部作らないのか

Week 11 の目的は、Socket.IO の基本をもう一度書くことではない。  
今回の目的は、既存のチャットアプリに新しい機能を追加する練習である。

実際のWebアプリ開発でも、毎回ゼロから作るのではなく、すでにあるコードを読んで、必要な部分を追加・変更することが多い。

そのため、この課題では次の流れで進める。

```text
Step 0：まず動くコードを確認する
Step 1：画面を見やすくする
Step 2：ログイン機能を追加する
Step 3：ユーザー一覧を追加する
Step 4：個別メッセージを追加する
```

---

### 2.4 Step 0 でまだできないこと

Step 0 のコードでは、まだ次のことはできない。

- ユーザー名を入力してログインする
- 同じユーザー名を禁止する
- 現在接続中のユーザーを表示する
- 特定のユーザーにだけメッセージを送る
- メッセージ受信時に自動スクロールする

これらは、Step 2、Step 3、Step 4 で追加する。

!!! note "重要"
    Step 0 は「配布された完成コード」ではなく、「Week 11 のスタート地点」である。  
    まず Step 0 を実行し、そこから各 Step の変更点を追加していく。

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
│       └── App.js
└── server/
    ├── package.json
    └── server.js
```

編集するファイルは、主に次の2つである。

| ファイル | 役割 |
|---|---|
| `client/src/App.js` | React 側の画面とクライアント処理を書く |
| `server/server.js` | Express + Socket.IO のサーバー処理を書く |

---

<a id="vscode"></a>

## 4. VS Code ランチャーの準備

この方法を使うと、VS Code の「実行とデバッグ」から、クライアント（React）とサーバー（Express + Socket.IO）を同時に起動できる。

!!! note "このセクションについて"
    このセクションは、授業で配布された `.vscode` 用ファイルを使う場合の説明である。  
    ランチャーがうまく動かない場合は、次の [手動で実行する方法](#run) を使えばよい。

---

### 4.1 `.vscode` フォルダを作成する

`chatapp` フォルダの直下に `.vscode` フォルダを作成する。

正しい場所：

```text
chatapp/
├── .vscode/
├── client/
└── server/
```

間違った場所：

```text
chatapp/client/.vscode/
chatapp/server/.vscode/
```

!!! warning "重要"
    `.vscode` フォルダは、`client` や `server` の中ではなく、`chatapp` の直下に作成する。

---

### 4.2 3つのファイルを保存する

`.vscode` フォルダの中に、配布された次の3つのファイルを保存する。

```text
.vscode/
├── launch.json
├── tasks.json
└── settings.json
```

それぞれの役割は次の通りである。

| ファイル | 役割 |
|---|---|
| `launch.json` | VS Code の「実行とデバッグ」で、どのプログラムを起動するかを決める |
| `tasks.json` | `npm start` などのコマンドを VS Code から実行する |
| `settings.json` | このプロジェクト用の VS Code 設定を書く |

---

### 4.3 VS Code を再起動する

3つのファイルを保存したら、VS Code を一度閉じて、もう一度開く。

!!! note "理由"
    VS Code に新しい `.vscode` 設定を読み込ませるためである。

---

### 4.4 VS Code で開くフォルダを確認する

VS Code では、必ず `chatapp` フォルダを開く。

正しい例：

```text
chatapp/
```

間違いやすい例：

```text
chatapp/client/
chatapp/server/
```

!!! warning "注意"
    `client` フォルダだけ、または `server` フォルダだけを開くと、`launch.json` のパスが合わず、ランチャーが動かないことがある。

---

### 4.5 `launch.json` のパスを確認する

`launch.json` の中には、`server.js` の場所を示すパスが書かれている。

例：

```json
"program": "${workspaceFolder}/server/server.js"
```

これは、次の場所に `server.js` があるという意味である。

```text
chatapp/server/server.js
```

もし自分のフォルダ構成が違う場合は、`launch.json` の中のパスを変更する必要がある。

例えば、VS Code で `chatapp` の親フォルダを開いている場合、次のようなパスが必要になることがある。

```json
"program": "${workspaceFolder}/chatapp/server/server.js"
```

!!! note "おすすめ"
    パスが分からない場合は、VS Code で `chatapp` フォルダそのものを開き直すとよい。

---

### 4.6 VS Code ランチャーで実行する

1. VS Code で `chatapp` フォルダを開く
2. 左側の「実行とデバッグ」アイコンをクリックする
3. 上部メニューから `Launch Server (Express + Socket.IO)` を選択する
4. 実行ボタンをクリックする

これにより、以下が自動で起動する。

```text
Express サーバー（node server.js）
React アプリ（npm start）
```

ブラウザで次のURLを開く。

```text
http://localhost:3000
```

---

### 4.7 ランチャーが動かない場合

ランチャーが動かない場合は、無理に使わなくてよい。  
次の「手動で実行する方法」で起動できる。

よくある原因は次の通りである。

| 原因 | 対処 |
|---|---|
| VS Code で `chatapp` 以外のフォルダを開いている | `chatapp` フォルダを開き直す |
| `.vscode` が `client` や `server` の中にある | `.vscode` を `chatapp` の直下に移動する |
| `launch.json` のパスが違う | `server.js` の場所に合わせて修正する |
| すでにサーバーが起動している | 古いサーバーを止めてから実行する |

---

<a id="run"></a>

## 5. 手動で実行する方法

実行するときは、ターミナルを2つ使う。

---

### 5.1 サーバーを起動する

1つ目のターミナルで実行する。

```bash
cd server
node server.js
```

成功すると、次のように表示される。

```text
Server running at http://localhost:3001
```

---

### 5.2 クライアントを起動する

2つ目のターミナルで実行する。

```bash
cd client
npm start
```

ブラウザで次のURLが開く。

```text
http://localhost:3000
```

---

### 5.3 server.js を変更した場合

`server.js` を変更した場合は、サーバーを再起動する必要がある。

サーバーを動かしているターミナルで、次を押す。

```text
Ctrl + C
```

その後、もう一度実行する。

```bash
node server.js
```

!!! note "App.js と server.js の違い"
    `App.js` を変更した場合は、保存すると自動的にブラウザへ反映されることが多い。  
    しかし、`server.js` を変更した場合は、必ずサーバーを再起動する必要がある。

---

<a id="step0"></a>

## 6. Step 0：プレーンなチャットアプリを実行する

Step 0 では、Bootstrap を使わないプレーンなチャットアプリを実行する。

このコードは、Week 11 の作業を始めるための土台である。  
Week 10 で学んだ基本的な Socket.IO チャットを、今回の拡張用に整理したものである。

この時点では、ログイン機能もユーザー一覧もない。  
まずは、Socket.IO でメッセージを送受信できることを確認する。

---

### 6.1 Step 0 の App.js

`client/src/App.js` を次のコードに置き換える。

```js
import React, { useEffect, useRef, useState } from 'react';
import { io } from 'socket.io-client';

function App() {
  const socketRef = useRef(null);

  const [username, setUsername] = useState(''); // Step 2 のログイン機能で使う
  const [chatLog, setChatLog] = useState([]);
  const [inputMessage, setInputMessage] = useState('');

  useEffect(() => {
    socketRef.current = io('http://localhost:3001');

    socketRef.current.on('receive_message', (data) => {
      console.log('Received message:', data);
      setChatLog((prev) => [...prev, data]);
    });

    return () => {
      socketRef.current.off('receive_message');
      socketRef.current.disconnect();
    };
  }, []);

  const sendMessage = () => {
    if (inputMessage.trim() !== '') {
      const message = {
        from: username,
        text: inputMessage.trim(),
        type: 'text',
        time: Date.now(),
      };

      console.log('Sending message:', message);
      socketRef.current.emit('send_message', message);
      setInputMessage('');
    }
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial' }}>
      <h2>Socket.IO Chat App (Step 0)</h2>
      <h3>Welcome, {username}</h3>

      <div
        style={{
          border: '1px solid #ccc',
          padding: '1rem',
          height: '300px',
          overflowY: 'scroll',
          marginBottom: '1rem',
        }}
      >
        {chatLog.map((msg, idx) => (
          <div key={idx} style={{ marginBottom: '0.5rem' }}>
            [{msg.from}] {msg.text}
          </div>
        ))}
      </div>

      <input
        type="text"
        value={inputMessage}
        onChange={(e) => setInputMessage(e.target.value)}
        placeholder="Type a message..."
      />

      <button onClick={sendMessage}>
        Send
      </button>
    </div>
  );
}

export default App;
```

---

### 6.2 Step 0 の server.js

`server/server.js` を次のコードに置き換える。

```js
const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const path = require('path');

const app = express();
const server = http.createServer(app);

const io = new Server(server, {
  cors: { origin: '*' }
});

app.use(express.static(path.join(__dirname, 'client')));

io.on('connection', (socket) => {
  console.log('User connected:', socket.id);

  // send_message イベントを受け取る
  socket.on('send_message', (data) => {
    const fullMessage = {
      from: data.from,
      text: data.text,
      type: data.type,
      time: data.time,
    };

    console.log(`User ${socket.id} (${data.from}) says: ${data.text}`);
    io.emit('receive_message', fullMessage); // 全員に送信する
  });
});

const PORT = process.env.PORT || 3001;

server.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
```

---

### 6.3 Step 0 の確認

1. サーバーを起動する
2. クライアントを起動する
3. ブラウザを2つ開く
4. 片方の画面でメッセージを送る
5. 両方の画面にメッセージが表示されることを確認する

!!! warning "この時点での注意"
    Step 0 では、`username` が空である。  
    そのため、メッセージが `[] Hello` のように表示される場合がある。  
    これはエラーではない。Step 2 でログイン機能を追加すると解決する。

---

<a id="step1"></a>

## 7. Step 1：Bootstrap で画面をスタイリングする

Step 1 では、Step 0 のチャットアプリに Bootstrap を追加し、画面を見やすくする。

!!! note "Step 1 で行うこと"
    Step 1 で変更するのは `App.js` だけである。  
    `server.js` は Step 0 のままでよい。

---

### 7.1 Bootstrap をインストールする

Bootstrap は React 側で使うため、`client` フォルダでインストールする。

```bash
cd client
npm install bootstrap
```

!!! warning "重要"
    Bootstrap のインストールは、この1回だけでよい。  
    Step 2、Step 3、Step 4 で何度も実行する必要はない。

---

### 7.2 App.js：Bootstrap を読み込む

`App.js` の上の import 部分に、次を追加する。

```js
import 'bootstrap/dist/css/bootstrap.min.css';
```

変更前：

```js
import React, { useEffect, useRef, useState } from 'react';
import { io } from 'socket.io-client';
```

変更後：

```js hl_lines="3"
import React, { useEffect, useRef, useState } from 'react';
import { io } from 'socket.io-client';
import 'bootstrap/dist/css/bootstrap.min.css';
```

---

### 7.3 App.js：return 部分を Bootstrap 版に置き換える

Step 0 の `return (` から最後の `);` までを、次のコードに置き換える。

ハイライトされている行が、Bootstrap に関係する新しい部分である。  
ハイライトされていない行は、チャットの基本処理として Step 0 から残っている部分である。

```js hl_lines="2 3 5 7 8 15 18 23"
return (
  <div className="container mt-3">
    <h4 className="mb-3">Welcome, {username}</h4>

    <div className="border rounded p-3 mb-3" style={{ height: '300px', overflowY: 'scroll' }}>
      {chatLog.map((msg, idx) => (
        <div key={idx} className={`mb-2 ${msg.from === username ? 'text-end' : 'text-start'}`}>
          <span className="badge bg-light text-dark">
            [{msg.from}] {msg.text}
          </span>
        </div>
      ))}
    </div>

    <div className="d-flex gap-2">
      <input
        type="text"
        className="form-control"
        value={inputMessage}
        onChange={(e) => setInputMessage(e.target.value)}
        placeholder="Type a message..."
      />

      <button className="btn btn-success" onClick={sendMessage}>
        Send
      </button>
    </div>
  </div>
);
```

---

### 7.4 追加・変更したコードの意味

| コード | 意味 |
|---|---|
| `container` | 画面全体に適切な余白をつける |
| `mt-3` | 上に余白をつける |
| `mb-3` | 下に余白をつける |
| `border` | 枠線を表示する |
| `rounded` | 角を丸くする |
| `p-3` | 内側に余白をつける |
| `form-control` | 入力欄を Bootstrap の見た目にする |
| `btn btn-success` | 緑色のボタンにする |
| `d-flex gap-2` | 入力欄とボタンを横並びにし、間に余白を入れる |
| `text-end` | 右寄せにする |
| `text-start` | 左寄せにする |

---

### 7.5 Step 1 の確認

1. クライアントを保存する
2. ブラウザを確認する
3. 入力欄とボタンが Bootstrap のデザインになっていることを確認する
4. メッセージ送受信が Step 0 と同じように動くことを確認する

!!! note "server.js について"
    Step 1 では、サーバー側の処理は変わらない。  
    したがって、`server.js` を変更する必要はない。

---

<a id="step2"></a>

## 8. Step 2：ログイン機能を追加する

Step 2 では、ユーザーが名前を入力してログインできるようにする。

ログイン後だけチャット画面を表示し、同じユーザー名は使えないようにする。

---

### 8.1 Step 2 で追加・変更する内容

`App.js` では、次を行う。

- ログイン用 state を追加する
- ログインボタンを押したときの関数を追加する
- サーバーから `login_success` と `login_error` を受け取る
- ログイン前はログイン画面だけを表示する
- メッセージ送信時、送信者名はサーバー側で判断するようにする

`server.js` では、次を行う。

- `users` という `Map` を追加する
- `login` イベントを追加する
- 同じユーザー名が使われていないか確認する
- `send_message` の中で、送信者名を `socket.id` から取得する
- 切断時にユーザー情報を削除する

---

### 8.2 App.js：ログイン用 state を追加・変更する

Step 1 の state 部分には、次のようなコードがある。

```js
const [username, setUsername] = useState('');
const [chatLog, setChatLog] = useState([]);
const [inputMessage, setInputMessage] = useState('');
```

これを次のように変更する。

```js hl_lines="1 3"
const [inputUsername, setInputUsername] = useState('');
const [username, setUsername] = useState('');
const [isLoggedIn, setIsLoggedIn] = useState(false);

const [chatLog, setChatLog] = useState([]);
const [inputMessage, setInputMessage] = useState('');
```

---

### 8.3 追加した state の意味

| state | 意味 |
|---|---|
| `inputUsername` | ログイン画面で入力中のユーザー名 |
| `username` | ログイン成功後に使うユーザー名 |
| `isLoggedIn` | ログイン済みかどうかを表す |

---

### 8.4 App.js：useEffect に login_success と login_error を追加する

Step 1 の `useEffect` の中には、`receive_message` の処理がある。

その下に、次を追加する。

```js hl_lines="1-8"
socketRef.current.on('login_success', (uname) => {
  setUsername(uname);
  setIsLoggedIn(true);
});

socketRef.current.on('login_error', (msg) => {
  alert(msg);
});
```

`return` の cleanup 部分には、次を追加する。

```js hl_lines="1-2"
socketRef.current.off('login_success');
socketRef.current.off('login_error');
```

変更後の `useEffect` は次のようになる。

```js hl_lines="9-16 20-21"
useEffect(() => {
  socketRef.current = io('http://localhost:3001');

  socketRef.current.on('receive_message', (data) => {
    console.log('Received message:', data);
    setChatLog((prev) => [...prev, data]);
  });

  socketRef.current.on('login_success', (uname) => {
    setUsername(uname);
    setIsLoggedIn(true);
  });

  socketRef.current.on('login_error', (msg) => {
    alert(msg);
  });

  return () => {
    socketRef.current.off('receive_message');
    socketRef.current.off('login_success');
    socketRef.current.off('login_error');
    socketRef.current.disconnect();
  };
}, []);
```

---

### 8.5 login_success と login_error の意味

| イベント | 意味 |
|---|---|
| `login_success` | サーバーから「ログイン成功」と返ってきたときのイベント |
| `login_error` | サーバーから「ログイン失敗」と返ってきたときのイベント |

`login_success` を受け取ると、次の2つを行う。

```js
setUsername(uname);
setIsLoggedIn(true);
```

これにより、ユーザー名が保存され、チャット画面に進む。

---

### 8.6 App.js：handleLogin 関数を追加する

`sendMessage` 関数の上に、次を追加する。

```js hl_lines="1-5"
const handleLogin = () => {
  if (inputUsername.trim() !== '') {
    socketRef.current.emit('login', inputUsername.trim());
  }
};
```

この関数は、入力されたユーザー名をサーバーに送る。

```js
socketRef.current.emit('login', inputUsername.trim());
```

---

### 8.7 App.js：sendMessage 関数を変更する

Step 1 の `sendMessage` では、クライアント側から `from: username` を送っていた。

Step 2 では、送信者名はサーバー側で判断するため、`sendMessage` を次のように変更する。

```js hl_lines="3-7"
const sendMessage = () => {
  if (inputMessage.trim() !== '') {
    socketRef.current.emit('send_message', {
      text: inputMessage.trim(),
      type: 'text',
      time: Date.now(),
    });

    setInputMessage('');
  }
};
```

!!! note "なぜ from を送らないのか"
    クライアントから `from` を送ると、別の名前を送ることもできてしまう。  
    サーバー側で `socket.id` からユーザー名を取得する方が安全である。

---

### 8.8 App.js：ログイン画面を追加する

チャット画面の `return (` より前に、次を追加する。

```js hl_lines="1-19"
if (!isLoggedIn) {
  return (
    <div className="container mt-5">
      <h3>Login to Chat</h3>

      <input
        className="form-control mb-2"
        type="text"
        value={inputUsername}
        onChange={(e) => setInputUsername(e.target.value)}
        placeholder="Enter username"
      />

      <button className="btn btn-primary" onClick={handleLogin}>
        Login
      </button>
    </div>
  );
}
```

このコードにより、ログイン前はチャット画面ではなく、ログイン画面だけが表示される。

---

### 8.9 server.js：users Map を追加する

`server.js` の上部で、`app.use(...)` の下に次を追加する。

```js hl_lines="1"
const users = new Map(); // socket.id → username を管理
```

`users` は、接続しているユーザーを管理するための変数である。

```text
socket.id → username
```

例：

```text
abc123 → UserA
def456 → UserB
```

---

### 8.10 server.js：login イベントを追加する

`io.on('connection', (socket) => { ... })` の中に、次を追加する。  
場所は、`send_message` より上が分かりやすい。

```js hl_lines="1-13"
socket.on('login', (username) => {
  for (let name of users.values()) {
    if (name === username) {
      socket.emit('login_error', 'Username already in use. Please choose a different name.');
      return;
    }
  }

  users.set(socket.id, username);
  console.log(`User logged in: ${username} (Socket ID: ${socket.id})`);
  socket.emit('login_success', username);
});
```

---

### 8.11 login イベントの意味

| コード | 意味 |
|---|---|
| `socket.on('login', ...)` | クライアントからログイン要求を受け取る |
| `users.values()` | 現在使われているユーザー名を確認する |
| `name === username` | 同じユーザー名があるか確認する |
| `socket.emit('login_error', ...)` | 同じ名前がある場合、エラーを本人に送る |
| `users.set(socket.id, username)` | ログイン成功時に、socket.id と username を保存する |
| `socket.emit('login_success', username)` | ログイン成功を本人に送る |

---

### 8.12 server.js：send_message を変更する

Step 1 の `send_message` を、次のように置き換える。

```js hl_lines="2 5"
socket.on('send_message', (data) => {
  const sender = users.get(socket.id);

  const fullMessage = {
    from: sender || 'unknown',
    text: data.text,
    type: data.type,
    time: data.time,
  };

  io.emit('receive_message', fullMessage);
});
```

ここでは、送信者名を `users.get(socket.id)` で取得している。

---

### 8.13 server.js：disconnect を追加する

`io.on('connection', (socket) => { ... })` の中に、次を追加する。

```js hl_lines="1-4"
socket.on('disconnect', () => {
  console.log('User disconnected:', socket.id);
  users.delete(socket.id);
});
```

ユーザーがブラウザを閉じたり接続が切れたりしたときに、`users` から削除する。

---

### 8.14 Step 2 の確認

1. サーバーを再起動する
2. クライアントを開く
3. ログイン画面が表示されることを確認する
4. ユーザー名を入力してログインする
5. ログイン後にチャット画面が表示されることを確認する
6. 別ブラウザで同じユーザー名を使う
7. エラーが表示されることを確認する

---

<a id="step3"></a>

## 9. Step 3：接続中ユーザー一覧を表示する

Step 3 では、現在ログインしているユーザー一覧を画面右側に表示する。

---

### 9.1 Step 3 で追加・変更する内容

`server.js` では、次を行う。

- ユーザー一覧を全員に送る関数 `broadcastUserList()` を追加する
- ログイン成功後にユーザー一覧を送る
- 切断時にもユーザー一覧を更新する

`App.js` では、次を行う。

- `userList` state を追加する
- `userlist` イベントを受け取る
- チャット画面を左右2列にして、右側にユーザー一覧を表示する

---

### 9.2 server.js：broadcastUserList 関数を追加する

`const users = new Map();` の下に、次を追加する。

```js hl_lines="1-4"
function broadcastUserList() {
  const userList = Array.from(users.values());
  io.emit('userlist', { type: 'userlist', userlist: userList });
}
```

---

### 9.3 broadcastUserList の意味

| コード | 意味 |
|---|---|
| `users.values()` | `Map` からユーザー名だけを取り出す |
| `Array.from(...)` | 取り出したユーザー名を配列にする |
| `io.emit('userlist', ...)` | 全員にユーザー一覧を送る |

例えば、`users` に `UserA` と `UserB` が入っている場合、次のような配列を送る。

```js
["UserA", "UserB"]
```

---

### 9.4 server.js：ログイン後にユーザー一覧を送る

Step 2 の `login` イベントの中で、次の行を探す。

```js
socket.emit('login_success', username);
```

その直後に、次を追加する。

```js
broadcastUserList();
```

変更後：

```js hl_lines="2"
socket.emit('login_success', username);
broadcastUserList();
```

これにより、新しいユーザーがログインした直後に、全員のユーザー一覧が更新される。

---

### 9.5 server.js：disconnect を変更する

Step 2 の `disconnect` を、次のコードに置き換える。

```js hl_lines="2 4-10"
socket.on('disconnect', () => {
  const username = users.get(socket.id);

  if (username) {
    console.log(`User disconnected: ${username} (${socket.id})`);
    users.delete(socket.id);
    broadcastUserList();
  } else {
    console.log('User disconnected:', socket.id);
  }
});
```

切断時にも `broadcastUserList()` を呼ぶことで、残っているユーザーの画面が更新される。

---

### 9.6 App.js：userList state を追加する

Step 2 の state 部分に、次を追加する。

```js hl_lines="1"
const [userList, setUserList] = useState([]);
```

例：

```js hl_lines="3"
const [chatLog, setChatLog] = useState([]);
const [inputMessage, setInputMessage] = useState('');
const [userList, setUserList] = useState([]);
```

---

### 9.7 App.js：userlist イベントを受け取る

`useEffect` の中で、`login_error` の処理の下に次を追加する。

```js hl_lines="1-5"
socketRef.current.on('userlist', (data) => {
  if (Array.isArray(data.userlist)) {
    setUserList(data.userlist);
  }
});
```

cleanup 部分にも、次を追加する。

```js hl_lines="1"
socketRef.current.off('userlist');
```

変更後の cleanup の例：

```js hl_lines="5"
return () => {
  socketRef.current.off('receive_message');
  socketRef.current.off('login_success');
  socketRef.current.off('login_error');
  socketRef.current.off('userlist');
  socketRef.current.disconnect();
};
```

---

### 9.8 userlist イベントの意味

サーバーは、現在ログイン中のユーザー一覧を次の形で送る。

```js
{
  type: 'userlist',
  userlist: ['UserA', 'UserB']
}
```

クライアント側では、`data.userlist` が配列であることを確認してから、`setUserList()` で保存する。

---

### 9.9 App.js：チャット表示部分を2列に変更する

Step 2 のチャットログ表示部分を、次のコードに置き換える。

```js hl_lines="1 3 17-33"
<div className="row">
  <div
    className="col-md-8 border rounded p-3 mb-3"
    style={{ height: '300px', overflowY: 'scroll' }}
  >
    {chatLog.map((msg, idx) => (
      <div
        key={idx}
        className={`mb-2 ${msg.from === username ? 'text-end' : 'text-start'}`}
      >
        <span className="badge bg-light text-dark">
          [{msg.from}] {msg.text}
        </span>
      </div>
    ))}
  </div>

  <div
    className="col-md-4 border rounded p-3 mb-3"
    style={{ height: '300px', overflowY: 'scroll' }}
  >
    <h5>Online Users</h5>

    <ul className="list-group">
      {userList.map((user) => (
        <li
          key={user}
          className={`list-group-item ${user === username ? 'active' : ''}`}
        >
          {user}
        </li>
      ))}
    </ul>
  </div>
</div>
```

---

### 9.10 追加した UI コードの意味

| コード | 意味 |
|---|---|
| `row` | 横並びのレイアウトを作る |
| `col-md-8` | 左側にチャット欄を表示する |
| `col-md-4` | 右側にユーザー一覧を表示する |
| `userList.map(...)` | ユーザー一覧を1人ずつ表示する |
| `list-group` | Bootstrap のリストデザインを使う |
| `user === username ? 'active' : ''` | 自分の名前だけ強調表示する |

---

### 9.11 Step 3 の確認

1. サーバーを再起動する
2. ブラウザを2つ開く
3. 1つ目で `UserA` としてログインする
4. 2つ目で `UserB` としてログインする
5. 両方の画面の右側に `UserA` と `UserB` が表示されることを確認する
6. 片方のブラウザを閉じる
7. 残った画面のユーザー一覧が更新されることを確認する

---

<a id="step4"></a>

## 10. Step 4：特定ユーザーへのメッセージ送信を追加する

Step 4 では、送信先を選べるようにする。

送信先は次の2種類である。

| 送信先 | 意味 |
|---|---|
| `*` | 全員 |
| ユーザー名 | 特定のユーザー |

また、メッセージ受信時にチャット欄の一番下まで自動スクロールする機能も追加する。

---

### 10.1 Step 4 で追加・変更する内容

`App.js` では、次を行う。

- `chatEndRef` を追加する
- `chatTo` state を追加する
- メッセージ受信時に自動スクロールする `useEffect` を追加する
- `sendMessage()` に `to` を追加する
- 送信先を選ぶ `select` を追加する
- メッセージ表示に送信先を表示する

`server.js` では、次を行う。

- `send_message` を書き換える
- `to === '*'` のときは全員に送る
- `to` が特定ユーザー名のときは、そのユーザーだけに送る
- 個別メッセージの場合、自分の画面にも表示する

---

### 10.2 App.js：chatEndRef を追加する

`socketRef` の下に、次を追加する。

```js hl_lines="1"
const chatEndRef = useRef(null);
```

変更後：

```js hl_lines="2"
const socketRef = useRef(null);
const chatEndRef = useRef(null);
```

`chatEndRef` は、チャット欄の一番下を指すために使う。

---

### 10.3 App.js：chatTo state を追加する

他の state と同じ場所に、次を追加する。

```js hl_lines="1"
const [chatTo, setChatTo] = useState('*'); // * = 全員
```

`chatTo` は、現在選ばれている送信先を保存する state である。

---

### 10.4 App.js：自動スクロール用 useEffect を追加する

最初の `useEffect` の下に、次を追加する。

```js hl_lines="1-3"
useEffect(() => {
  chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
}, [chatLog]);
```

`chatLog` が変わるたびに、チャット欄の一番下までスクロールする。

---

### 10.5 App.js：sendMessage を変更する

Step 3 の `sendMessage` を、次のコードに置き換える。

```js hl_lines="4-5"
const sendMessage = () => {
  if (inputMessage.trim() !== '') {
    socketRef.current.emit('send_message', {
      from: username, // 表示用
      to: chatTo,
      text: inputMessage.trim(),
      type: 'text',
      time: Date.now(),
    });

    setInputMessage('');
  }
};
```

重要な追加部分は次である。

```js
to: chatTo
```

これにより、メッセージに送信先情報が含まれる。

---

### 10.6 App.js：メッセージ表示に送信先を追加する

Step 3 では、メッセージ表示が次のようになっている。

```js
[{msg.from}] {msg.text}
```

これを次のように変更する。

```js hl_lines="1"
[{msg.from} ➝ {msg.to === '*' ? 'Everyone' : msg.to}] {msg.text}
```

これにより、誰から誰へのメッセージかが分かる。

---

### 10.7 App.js：チャット欄の一番下に ref を追加する

チャットログの `map` が終わった後に、次を追加する。

```js hl_lines="1"
<div ref={chatEndRef} />
```

例：

```js hl_lines="7 12"
{chatLog.map((msg, idx) => (
  <div
    key={idx}
    className={`mb-2 ${msg.from === username ? 'text-end' : 'text-start'}`}
  >
    <span className="badge bg-light text-dark">
      [{msg.from} ➝ {msg.to === '*' ? 'Everyone' : msg.to}] {msg.text}
    </span>
  </div>
))}

<div ref={chatEndRef} />
```

---

### 10.8 App.js：送信先を選ぶ select を追加する

入力欄と Send ボタンの上に、次を追加する。

```js hl_lines="1-17"
<div className="mb-2">
  <select
    className="form-select w-auto"
    value={chatTo}
    onChange={(e) => setChatTo(e.target.value)}
  >
    <option value="*">Everyone (*)</option>

    {userList
      .filter((u) => u !== username)
      .map((u) => (
        <option key={u} value={u}>
          {u}
        </option>
      ))}
  </select>
</div>
```

---

### 10.9 select の意味

| コード | 意味 |
|---|---|
| `<option value="*">Everyone (*)</option>` | 全員宛て |
| `userList.filter((u) => u !== username)` | 自分以外のユーザーだけを選択肢にする |
| `.map((u) => ...)` | ユーザー名ごとに option を作る |
| `value={chatTo}` | 現在選ばれている送信先 |
| `onChange={...}` | 選択が変わったときに `chatTo` を更新する |

---

### 10.10 server.js：send_message を書き換える

Step 3 の `send_message` を、次のコードに置き換える。

```js hl_lines="5-6 11-25 27"
socket.on('send_message', (data) => {
  const sender = users.get(socket.id) || 'anonymous';

  const fullMessage = {
    from: sender,
    to: data.to,
    text: data.text,
    type: data.type,
    time: data.time,
  };

  if (data.to === '*') {
    // 全体に送信
    io.emit('receive_message', fullMessage);
  } else {
    // 相手のソケットを探して送信
    for (let [id, name] of users.entries()) {
      if (name === data.to) {
        io.to(id).emit('receive_message', fullMessage);
        break;
      }
    }

    // 自分にも表示
    socket.emit('receive_message', fullMessage);
  }

  console.log(`[${sender} ➝ ${data.to}] ${data.text}`);
});
```

---

### 10.11 個別メッセージの仕組み

個別メッセージでは、サーバーが `users` の中から送信先を探す。

```js hl_lines="1-6"
for (let [id, name] of users.entries()) {
  if (name === data.to) {
    io.to(id).emit('receive_message', fullMessage);
    break;
  }
}
```

このコードの意味は次の通りである。

1. `users.entries()` で、すべての `socket.id` とユーザー名を取り出す
2. `name === data.to` で、送信先のユーザー名と一致するか確認する
3. 一致したら、`io.to(id).emit(...)` でそのユーザーだけに送る
4. 見つかったら `break` でループを終了する

---

### 10.12 なぜ自分にも送るのか

個別メッセージの場合、受信者だけに送ると、送信者の画面には自分が送ったメッセージが表示されない。

そのため、次のコードで送信者自身にも表示している。

```js hl_lines="1"
socket.emit('receive_message', fullMessage);
```

---

### 10.13 Step 4 の確認

1. サーバーを再起動する
2. ブラウザを2つ以上開く
3. `UserA` と `UserB` でログインする
4. `Everyone (*)` を選んで送信し、全員に表示されることを確認する
5. `UserA` から `UserB` を選んで送信する
6. `UserA` と `UserB` の画面だけに表示されることを確認する
7. メッセージが増えたとき、一番下まで自動スクロールすることを確認する

---

<a id="step5"></a>

## 11. Step 5：チャレンジ・任意

時間がある場合は、次のような機能を追加してもよい。

---

### 11.1 Enter キーで送信

メッセージ入力欄に次を追加する。

```js hl_lines="1-5"
onKeyDown={(e) => {
  if (e.key === 'Enter') {
    sendMessage();
  }
}}
```

---

### 11.2 自分のメッセージの色を変える

メッセージ表示の `span` を、次のように変更する。

```js hl_lines="1-3"
<span
  className={msg.from === username ? 'badge bg-primary text-white' : 'badge bg-light text-dark'}
>
```

---

### 11.3 ログアウトボタン

ログアウトボタンを追加し、押したときにログイン状態をリセットする。

例：

```js hl_lines="1-6"
const handleLogout = () => {
  setIsLoggedIn(false);
  setUsername('');
  setInputUsername('');
  setChatLog([]);
};
```

---

<a id="trouble"></a>

## 12. よくあるエラー

---

### 12.1 `EADDRINUSE` または `address already in use`

原因：すでにサーバーが動いている。

Mac の場合、次で 3001 番ポートを使っているプロセスを確認する。

```bash
lsof -i :3001
```

`node` の PID を確認し、次のように停止する。

```bash
kill -9 PID番号
```

例：

```bash
kill -9 62635
```

その後、もう一度サーバーを起動する。

```bash
node server.js
```

---

### 12.2 Bootstrap のエラー

次のようなエラーが出る場合：

```text
Module not found: Can't resolve 'bootstrap/dist/css/bootstrap.min.css'
```

`client` フォルダで Bootstrap がインストールされていない。

```bash
cd client
npm install bootstrap
```

---

### 12.3 メッセージが表示されない

確認すること：

- サーバーが起動しているか
- クライアントが起動しているか
- `App.js` の接続先が `http://localhost:3001` になっているか
- イベント名が一致しているか

使うイベント名：

```text
send_message
receive_message
login
login_success
login_error
userlist
```

---

### 12.4 ユーザー一覧が表示されない

確認すること：

- `server.js` に `broadcastUserList()` があるか
- ログイン後に `broadcastUserList()` を呼んでいるか
- 切断時に `broadcastUserList()` を呼んでいるか
- `App.js` で `userlist` イベントを受け取っているか
- `userList.map(...)` で画面に表示しているか

---

<a id="student-info"></a>

## 13. 提出前に：名前と学籍番号を画面上部に表示する

提出前に、React アプリの画面上部に自分の名前と学籍番号を表示すること。

これは、提出されたスクリーンショットが本人のものであることを確認するためである。

---

### 13.1 App.js に追加する場所

チャット画面の一番上に表示したいので、ログイン後の `return` の中で、次のような場所に追加する。

```js hl_lines="3-6"
return (
  <div className="container mt-3">
    <div className="alert alert-secondary">
      名前：立命 太郎 ／ 学籍番号：123456789
    </div>

    <h4 className="mb-3">Welcome, {username}</h4>

    ...
  </div>
);
```

---

### 13.2 自分の情報に書き換える

上の例をそのまま使わず、自分の名前と学籍番号に書き換えること。

例：

```js
名前：立命 太郎 ／ 学籍番号：260000000
```

!!! warning "注意"
    `立命 太郎` や `123456789` のまま提出しないこと。  
    必ず自分の名前と学籍番号に変更する。

---

<a id="submission"></a>

## 14. 提出方法

提出先は **Moodle+R** である。

提出するものは、次の3つである。

```text
App.js
server.js
スクリーンショット
```

---

### 14.1 提出ファイル

次の2つのファイルを提出する。

| ファイル | 場所 |
|---|---|
| `App.js` | `client/src/App.js` |
| `server.js` | `server/server.js` |

提出形式は、次のどちらかでよい。

```text
.js
.txt
```

---

### 14.2 スクリーンショット

チャットアプリを実行し、画面のスクリーンショットを提出する。

スクリーンショットには、次の内容が見えるようにすること。

- 名前
- 学籍番号
- チャット画面
- ログイン中のユーザー名
- 接続中ユーザー一覧
- 送信先選択のドロップダウン

!!! warning "重要"
    スクリーンショットの画面上部に、名前と学籍番号が表示されていること。  
    名前と学籍番号が表示されていないスクリーンショットは、提出条件を満たしていない。

---

### 14.3 提出しないもの

次のものは提出しない。

```text
node_modules
.vscode
package-lock.json
package.json
```

提出するのは、`App.js`、`server.js`、スクリーンショットのみである。

---

### 14.4 提出前チェックリスト

提出前に、次を確認すること。

- [ ] `App.js` を提出する
- [ ] `server.js` を提出する
- [ ] スクリーンショットを提出する
- [ ] スクリーンショットに名前が表示されている
- [ ] スクリーンショットに学籍番号が表示されている
- [ ] チャット画面が表示されている
- [ ] ユーザー一覧が表示されている
- [ ] 個別メッセージの送信先選択が表示されている
