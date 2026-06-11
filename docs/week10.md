# Week 10: Introduction to Socket.IO

このページでは、Socket.IO を用いて、簡単なリアルタイムチャットアプリを作成する。

Week 10 では、次の4つの Step を順番に実装する。

- Step 1: サーバーから Reactクライアントにメッセージを送る
- Step 2: Reactクライアントからサーバーにメッセージを送る
- Step 3: 匿名チャットを作成する
- Step 4: 名前付きチャットを作成する

!!! important
    ミニ課題10として提出するのは **Step 4 の完成版のみ** である。

    Step 1〜Step 3 は練習用である。ただし、Step 4 を理解するために、順番に実装することを推奨する。

---

## 1. この週で学ぶこと

Week 10 では、リアルタイム通信の基本を学ぶ。

通常の Web アプリケーションでは、ブラウザがサーバーにリクエストを送り、サーバーがレスポンスを返す。

```text
Browser → Server → Response
```

しかし、チャットアプリでは、あるユーザーがメッセージを送ったときに、他のユーザーの画面にもすぐにメッセージを表示する必要がある。

このような処理には、サーバーからクライアントにデータを送る仕組みが必要である。

この授業では、そのために **Socket.IO** を使う。

---

## 2. Socket.IO の基本的な考え方

### 2.1 Socket.IO とは

Socket.IO は、サーバーとクライアントの間でリアルタイム通信を行うための JavaScript ライブラリである。

Socket.IO を使うと、次のような通信ができる。

- サーバーからクライアントにメッセージを送る
- クライアントからサーバーにメッセージを送る
- サーバーからすべてのクライアントにメッセージを送る

---

### 2.2 `emit` と `on`

Socket.IO では、イベント名を使ってデータを送受信する。

データを送るときは `emit` を使う。

```javascript
socket.emit('event_name', data);
```

データを受け取るときは `on` を使う。

```javascript
socket.on('event_name', (data) => {
  // received data
});
```

!!! note
    `emit` は「送る」と考えるとよい。

    `on` は「受け取る準備をする」と考えるとよい。

---

### 2.3 `socket.emit` と `io.emit`

Socket.IO では、「誰に送るか」によって使うコードが変わる。

| Code | 意味 |
|---|---|
| `socket.emit(...)` | 1人のクライアントに送る |
| `io.emit(...)` | 接続しているすべてのクライアントに送る |
| `socket.on(...)` | イベントを受け取る |

たとえば、サーバーから、今接続したクライアントだけにメッセージを送る場合は、次のように書く。

```javascript
socket.emit('welcome', 'Welcome!');
```

接続している全員にメッセージを送る場合は、次のように書く。

```javascript
io.emit('receive_message', 'Hello everyone!');
```

!!! note
    `socket.emit` は「1人に送る」と考えるとよい。

    `io.emit` は「全員に送る」と考えるとよい。

---

## 3. Week 10 で使うファイル

### 3.1 前提

このページを始める前に、Setup ページを完了している必要がある。

Setup が完了している場合、プロジェクトは次のようになっている。

```text
chatapp/
├── server/
│   └── server.js
└── client/
    └── src/
        └── App.js
```

---

### 3.2 編集するファイル

Week 10 で主に編集するファイルは、次の2つである。

| File | 目的 |
|---|---|
| `chatapp/server/server.js` | サーバー側のプログラムを書く |
| `chatapp/client/src/App.js` | Reactクライアント側のプログラムを書く |

---

### 3.3 起動するときに使うターミナル

この演習では、ターミナルを2つ使う。

| ターミナル | フォルダ | コマンド |
|---|---|---|
| ターミナル 1 | `chatapp/server` | `node server.js` |
| ターミナル 2 | `chatapp/client` | `npm start` |

!!! important
    `server.js` を変更した場合は、サーバーを再起動する必要がある。

    `App.js` を変更した場合は、保存すれば React が自動的に更新されることが多い。

---

## 4. Step 1: サーバーから Reactクライアントにメッセージを送る

### 4.1 Step 1 の目的

Step 1 では、Reactクライアントがサーバーに接続したときに、サーバーが welcome メッセージを送る。

流れは次の通りである。

```text
Reactクライアントがサーバーに接続する
        ↓
サーバーが connection を検出する
        ↓
サーバーが welcome イベントを送る
        ↓
Reactクライアントが welcome イベントを受け取る
        ↓
Reactクライアントが画面にメッセージを表示する
```

---

### 4.2 どのファイルを編集するか

Step 1 では、次の2つのファイルを編集する。

```text
chatapp/server/server.js
chatapp/client/src/App.js
```

---

### 4.3 `server.js` のコード

`chatapp/server/server.js` を開き、以下のコードに置き換える。

```javascript
const express = require('express');
const http = require('http');
const { Server } = require('socket.io');

const app = express();
const server = http.createServer(app);

const io = new Server(server, {
  cors: {
    origin: '*'
  }
});

io.on('connection', (socket) => {
  console.log('A user connected:', socket.id);

  socket.emit(
    'welcome',
    'Welcome! This is your first Socket.IO message.'
  );
});

const PORT = 3001;

server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

---

### 4.4 `server.js` の説明

```javascript
const express = require('express');
```

`express` を読み込んでいる。Express は Webサーバーを作るためのライブラリである。

---

```javascript
const http = require('http');
```

Node.js の `http` モジュールを読み込んでいる。

---

```javascript
const { Server } = require('socket.io');
```

Socket.IO の `Server` を読み込んでいる。

---

```javascript
const app = express();
```

Express アプリケーションを作成している。

---

```javascript
const server = http.createServer(app);
```

Express アプリケーションを使って HTTPサーバーを作成している。

---

```javascript
const io = new Server(server, {
  cors: {
    origin: '*'
  }
});
```

Socket.IO サーバーを作成している。

`cors: { origin: '*' }` は、異なる場所からの接続を許可する設定である。

React は通常 `http://localhost:3000` で動く。

サーバーは `http://localhost:3001` で動く。

ポート番号が違うため、この設定が必要である。

---

```javascript
io.on('connection', (socket) => {
```

クライアントが接続したときに実行される処理である。

`socket` は、接続してきた1つのクライアントを表す。

---

```javascript
socket.emit(
  'welcome',
  'Welcome! This is your first Socket.IO message.'
);
```

接続してきたクライアントに対して、`welcome` というイベント名でメッセージを送っている。

この場合、送られる相手は接続してきたクライアントだけである。

---

### 4.5 `App.js` のコード

`chatapp/client/src/App.js` を開き、以下のコードに置き換える。

```javascript
import React, { useEffect, useState } from 'react';
import { io } from 'socket.io-client';

const socket = io('http://localhost:3001');

function App() {
  const [msg, setMsg] = useState('');

  useEffect(() => {
    socket.on('welcome', (data) => {
      setMsg(data);
    });

    return () => {
      socket.off('welcome');
    };
  }, []);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h2>Socket.IO Chat App: Step 1</h2>

      <p>
        <strong>Server says:</strong> {msg}
      </p>
    </div>
  );
}

export default App;
```

---

### 4.6 `App.js` の説明

```javascript
import React, { useEffect, useState } from 'react';
```

React と、React の機能である `useEffect` と `useState` を読み込んでいる。

| Code | 意味 |
|---|---|
| `useState` | 画面に表示するデータを保存する |
| `useEffect` | ページが表示されたときなどに処理を実行する |

---

```javascript
import { io } from 'socket.io-client';
```

Socket.IO Client を読み込んでいる。

React からサーバーに接続するために必要である。

---

```javascript
const socket = io('http://localhost:3001');
```

Reactクライアントが Socket.IO サーバーに接続する。

---

```javascript
const [msg, setMsg] = useState('');
```

`msg` は、サーバーから受け取ったメッセージを保存するための state（状態変数）である。

`setMsg` は、`msg` の値を更新するための関数である。

---

```javascript
socket.on('welcome', (data) => {
  setMsg(data);
});
```

サーバーから `welcome` イベントを受け取ったときに実行される。

受け取ったデータを `msg` に保存する。

---

```javascript
return () => {
  socket.off('welcome');
};
```

`welcome` のイベントリスナーを解除する処理である。

---

### 4.7 Step 1 の実行方法

#### ターミナル 1: サーバー

`chatapp/server` に移動する。

```bash
cd chatapp/server
```

サーバーを起動する。

```bash
node server.js
```

次のように表示されればよい。

```text
Server running on port 3001
```

---

#### ターミナル 2: Reactクライアント

別のターミナルを開く。

`chatapp/client` に移動する。

```bash
cd chatapp/client
```

Reactクライアントを起動する。

```bash
npm start
```

ブラウザで次のように表示されれば成功である。

```text
Socket.IO Chat App: Step 1

Server says: Welcome! This is your first Socket.IO message.
```

---

## 5. Step 2: Reactクライアントからサーバーにメッセージを送る

### 5.1 Step 2 の目的

Step 2 では、ボタンをクリックしたときに、Reactクライアントからサーバーにメッセージを送る。

その後、サーバーは同じクライアントに返信する。

流れは次の通りである。

```text
ユーザーがボタンをクリックする
        ↓
Reactクライアントが hello イベントを送る
        ↓
サーバーが hello イベントを受け取る
        ↓
サーバーが response イベントを返す
        ↓
Reactクライアントが response を画面に表示する
```

---

### 5.2 `server.js` のコード

`chatapp/server/server.js` を以下のコードに置き換える。

```javascript
const express = require('express');
const http = require('http');
const { Server } = require('socket.io');

const app = express();
const server = http.createServer(app);

const io = new Server(server, {
  cors: {
    origin: '*'
  }
});

io.on('connection', (socket) => {
  console.log('A user connected:', socket.id);

  socket.emit(
    'welcome',
    'Welcome! This is your first Socket.IO message.'
  );

  socket.on('hello', () => {
    console.log(`User ${socket.id} said hello`);

    socket.emit(
      'response',
      'Hi! Server got your hello.'
    );
  });
});

const PORT = 3001;

server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

---

### 5.3 追加されたサーバー側のコード

Step 2 で新しく追加された部分は次である。

```javascript
socket.on('hello', () => {
  console.log(`User ${socket.id} said hello`);

  socket.emit(
    'response',
    'Hi! Server got your hello.'
  );
});
```

`socket.on('hello', ...)` は、クライアントから送られてくる `hello` イベントを待つ処理である。

クライアントが `hello` を送ると、サーバーは `response` イベントを返す。

ここでは `socket.emit` を使っているため、返信はそのクライアントのみに送られる。

---

### 5.4 `App.js` のコード

`chatapp/client/src/App.js` を以下のコードに置き換える。

```javascript
import React, { useEffect, useState } from 'react';
import { io } from 'socket.io-client';

const socket = io('http://localhost:3001');

function App() {
  const [msg, setMsg] = useState('');
  const [reply, setReply] = useState('');

  useEffect(() => {
    socket.on('welcome', (data) => {
      setMsg(data);
    });

    socket.on('response', (data) => {
      setReply(data);
    });

    return () => {
      socket.off('welcome');
      socket.off('response');
    };
  }, []);

  const handleClick = () => {
    socket.emit('hello');
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h2>Socket.IO Chat App: Step 2</h2>

      <p>
        <strong>Server says on connect:</strong> {msg}
      </p>

      <button onClick={handleClick}>
        Send Hello
      </button>

      <p>
        <strong>Server replied:</strong> {reply}
      </p>
    </div>
  );
}

export default App;
```

---

### 5.5 追加された React 側のコード

```javascript
const [reply, setReply] = useState('');
```

サーバーからの返信を保存するための state（状態変数）である。

---

```javascript
socket.on('response', (data) => {
  setReply(data);
});
```

サーバーから `response` イベントを受け取るための処理である。

---

```javascript
const handleClick = () => {
  socket.emit('hello');
};
```

ボタンがクリックされたときに、サーバーに `hello` イベントを送る。

---

```jsx
<button onClick={handleClick}>
  Send Hello
</button>
```

ボタンを表示している。

このボタンをクリックすると、`handleClick` が実行される。

---

### 5.6 Step 2 の実行方法

`server.js` を変更したため、サーバーを再起動する必要がある。

サーバーを動かしているターミナルで、次のキーを押す。

```text
Ctrl + C
```

その後、もう一度サーバーを起動する。

```bash
node server.js
```

`App.js` は保存するだけでよい。

ブラウザで `Send Hello` ボタンをクリックする。

次のように表示されれば成功である。

```text
Server replied: Hi! Server got your hello.
```

---

## 6. Step 3: 匿名チャットを作成する

### 6.1 Step 3 の目的

Step 3 では、テキストボックスに入力したメッセージをサーバーに送り、サーバーがすべてのクライアントに送信する。

この Step では、送信者の名前は表示しない。

そのため、匿名チャットである。

流れは次の通りである。

```text
ユーザーがメッセージを入力する
        ↓
Reactクライアントが send_message イベントを送る
        ↓
サーバーが send_message を受け取る
        ↓
サーバーが receive_message を全クライアントに送る
        ↓
すべてのクライアントがメッセージを表示する
```

---

### 6.2 `server.js` のコード

`chatapp/server/server.js` を以下のコードに置き換える。

```javascript
const express = require('express');
const http = require('http');
const { Server } = require('socket.io');

const app = express();
const server = http.createServer(app);

const io = new Server(server, {
  cors: {
    origin: '*'
  }
});

io.on('connection', (socket) => {
  console.log('A user connected:', socket.id);

  socket.emit(
    'welcome',
    'Welcome! This is your first Socket.IO message.'
  );

  socket.on('hello', () => {
    console.log(`User ${socket.id} said hello`);

    socket.emit(
      'response',
      'Hi! Server got your hello.'
    );
  });

  socket.on('send_message', (msg) => {
    console.log(`User ${socket.id} says:`, msg);

    io.emit(
      'receive_message',
      msg
    );
  });
});

const PORT = 3001;

server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

---

### 6.3 追加されたサーバー側のコード

Step 3 で新しく追加された部分は次である。

```javascript
socket.on('send_message', (msg) => {
  console.log(`User ${socket.id} says:`, msg);

  io.emit(
    'receive_message',
    msg
  );
});
```

`socket.on('send_message', ...)` は、クライアントから送られてくるチャットメッセージを受け取る処理である。

`msg` には、クライアントが送ったメッセージが入る。

次のコードで、接続しているすべてのクライアントにメッセージを送る。

```javascript
io.emit(
  'receive_message',
  msg
);
```

ここでは `socket.emit` ではなく `io.emit` を使う。

| Code | 意味 |
|---|---|
| `socket.emit` | 1人のクライアントに送る |
| `io.emit` | すべてのクライアントに送る |

---

### 6.4 `App.js` のコード

`chatapp/client/src/App.js` を以下のコードに置き換える。

```javascript
import React, { useEffect, useState } from 'react';
import { io } from 'socket.io-client';

const socket = io('http://localhost:3001');

function App() {
  const [msg, setMsg] = useState('');
  const [reply, setReply] = useState('');
  const [chatLog, setChatLog] = useState([]);
  const [input, setInput] = useState('');

  useEffect(() => {
    socket.on('welcome', (data) => {
      setMsg(data);
    });

    socket.on('response', (data) => {
      setReply(data);
    });

    socket.on('receive_message', (data) => {
      setChatLog((prev) => [...prev, data]);
    });

    return () => {
      socket.off('welcome');
      socket.off('response');
      socket.off('receive_message');
    };
  }, []);

  const handleClick = () => {
    socket.emit('hello');
  };

  const sendMessage = () => {
    if (input.trim() !== '') {
      socket.emit('send_message', input);
      setInput('');
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h2>Socket.IO Chat App: Step 3</h2>

      <p>
        <strong>Server says on connect:</strong> {msg}
      </p>

      <button onClick={handleClick}>
        Send Hello
      </button>

      <p>
        <strong>Server replied:</strong> {reply}
      </p>

      <hr />

      <h3>Anonymous Chat</h3>

      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type a message..."
      />

      <button onClick={sendMessage}>
        Send
      </button>

      <ul>
        {chatLog.map((item, idx) => (
          <li key={idx}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

---

### 6.5 追加された React 側のコード

```javascript
const [chatLog, setChatLog] = useState([]);
```

チャットのメッセージ一覧を保存するための state（状態変数）である。

`chatLog` は配列である。

例：

```javascript
['Hello', 'Good morning', 'Nice to meet you']
```

---

```javascript
const [input, setInput] = useState('');
```

テキストボックスに入力された文字を保存するための state（状態変数）である。

---

```javascript
socket.on('receive_message', (data) => {
  setChatLog((prev) => [...prev, data]);
});
```

サーバーから `receive_message` イベントを受け取ったときに実行される。

`setChatLog((prev) => [...prev, data])` は、以前のメッセージ一覧に新しいメッセージを追加する処理である。

---

```javascript
const sendMessage = () => {
  if (input.trim() !== '') {
    socket.emit('send_message', input);
    setInput('');
  }
};
```

この関数は、入力されたメッセージをサーバーに送る。

`input.trim() !== ''` は、空のメッセージを送らないための確認である。

---

```jsx
<input
  value={input}
  onChange={(e) => setInput(e.target.value)}
  placeholder="Type a message..."
/>
```

メッセージ入力用のテキストボックスである。

---

```jsx
<ul>
  {chatLog.map((item, idx) => (
    <li key={idx}>{item}</li>
  ))}
</ul>
```

`chatLog` に入っているメッセージを一覧表示する。

---

### 6.6 Step 3 の実行方法

`server.js` を変更したため、サーバーを再起動する。

サーバーを動かしているターミナルで、次のキーを押す。

```text
Ctrl + C
```

その後、もう一度サーバーを起動する。

```bash
node server.js
```

`App.js` は保存するだけでよい。

---

### 6.7 動作確認

ブラウザを2つ開く。

どちらも次の URL を開く。

```text
http://localhost:3000
```

1つ目のブラウザで、メッセージを入力する。

例：

```text
Hello
```

`Send` をクリックする。

両方のブラウザに次のように表示されれば成功である。

```text
Hello
```

---

## 7. Step 4: 名前付きチャットを作成する

### 7.1 Step 4 の目的

Step 4 では、メッセージに送信者の名前を表示する。

例：

```text
Alice: Hello
Bob: Hi Alice
Alice: Nice to meet you
```

この Step がミニ課題10の提出対象である。

---

### 7.2 Step 4 の流れ

処理の流れは次の通りである。

```text
ユーザーが名前を入力する
        ↓
ユーザーがメッセージを入力する
        ↓
Reactクライアントが name と message をサーバーに送る
        ↓
サーバーが name と message を組み合わせる
        ↓
サーバーが全クライアントに送る
        ↓
すべてのクライアントが名前付きメッセージを表示する
```

---

### 7.3 `server.js` のコード

`chatapp/server/server.js` を以下のコードに置き換える。

```javascript
const express = require('express');
const http = require('http');
const { Server } = require('socket.io');

const app = express();
const server = http.createServer(app);

const io = new Server(server, {
  cors: {
    origin: '*'
  }
});

io.on('connection', (socket) => {
  console.log('A user connected:', socket.id);

  socket.emit(
    'welcome',
    'Welcome! This is your first Socket.IO message.'
  );

  socket.on('hello', () => {
    console.log(`User ${socket.id} said hello`);

    socket.emit(
      'response',
      'Hi! Server got your hello.'
    );
  });

  socket.on('send_message', ({ name, message }) => {
    const fullMessage = `${name}: ${message}`;

    console.log(`User ${socket.id} says:`, fullMessage);

    io.emit(
      'receive_message',
      fullMessage
    );
  });
});

const PORT = 3001;

server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

---

### 7.4 Step 4 のサーバー側のポイント

Step 3 では、サーバーは1つの文字列を受け取っていた。

```javascript
socket.on('send_message', (msg) => {
```

Step 4 では、サーバーはオブジェクトを受け取る。

```javascript
socket.on('send_message', ({ name, message }) => {
```

React から送られるオブジェクトは次のような形である。

```javascript
{
  name: "Alice",
  message: "Hello"
}
```

サーバーでは、次のように名前とメッセージを1つの文字列にする。

```javascript
const fullMessage = `${name}: ${message}`;
```

結果は次のようになる。

```text
Alice: Hello
```

そして、全クライアントに送信する。

```javascript
io.emit(
  'receive_message',
  fullMessage
);
```

---

### 7.5 `App.js` のコード

`chatapp/client/src/App.js` を以下のコードに置き換える。

```javascript
import React, { useEffect, useState } from 'react';
import { io } from 'socket.io-client';

const socket = io('http://localhost:3001');

function App() {
  const [msg, setMsg] = useState('');
  const [reply, setReply] = useState('');
  const [chatLog, setChatLog] = useState([]);
  const [input, setInput] = useState('');
  const [name, setName] = useState('');

  useEffect(() => {
    socket.on('welcome', (data) => {
      setMsg(data);
    });

    socket.on('response', (data) => {
      setReply(data);
    });

    socket.on('receive_message', (data) => {
      setChatLog((prev) => [...prev, data]);
    });

    return () => {
      socket.off('welcome');
      socket.off('response');
      socket.off('receive_message');
    };
  }, []);

  const handleClick = () => {
    socket.emit('hello');
  };

  const sendMessage = () => {
    if (name.trim() !== '' && input.trim() !== '') {
      socket.emit(
        'send_message',
        {
          name: name,
          message: input
        }
      );

      setInput('');
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h2>Socket.IO Chat App: Step 4</h2>

      <p>
        <strong>Server says on connect:</strong> {msg}
      </p>

      <button onClick={handleClick}>
        Send Hello
      </button>

      <p>
        <strong>Server replied:</strong> {reply}
      </p>

      <hr />

      <h3>Named Chat</h3>

      <div>
        <input
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Enter your name"
        />
      </div>

      <br />

      <div>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message..."
        />

        <button onClick={sendMessage}>
          Send
        </button>
      </div>

      <ul>
        {chatLog.map((item, idx) => (
          <li key={idx}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

---

### 7.6 Step 4 の React 側のポイント

Step 4 では、名前を保存するための state（状態変数）を追加する。

```javascript
const [name, setName] = useState('');
```

---

名前入力用のテキストボックスを追加する。

```jsx
<input
  value={name}
  onChange={(e) => setName(e.target.value)}
  placeholder="Enter your name"
/>
```

---

メッセージを送る前に、名前とメッセージの両方が入力されているか確認する。

```javascript
if (name.trim() !== '' && input.trim() !== '') {
```

---

サーバーに送るデータをオブジェクトにする。

```javascript
socket.emit(
  'send_message',
  {
    name: name,
    message: input
  }
);
```

これは次のようなデータを送っているという意味である。

```javascript
{
  name: "Alice",
  message: "Hello"
}
```

---

!!! note "短い書き方"
    次のコードは、

    ```javascript
    {
      name: name,
      message: input
    }
    ```

    次のように短く書くこともできる。

    ```javascript
    {
      name,
      message: input
    }
    ```

    ただし、この授業では最初は分かりやすさを優先して、長い書き方を使っている。

---

### 7.7 Step 4 の実行方法

`server.js` を変更したため、サーバーを再起動する。

サーバーを動かしているターミナルで、次のキーを押す。

```text
Ctrl + C
```

その後、もう一度サーバーを起動する。

```bash
node server.js
```

`App.js` は保存するだけでよい。

---

### 7.8 動作確認

ブラウザを2つ開く。

どちらも次の URL を開く。

```text
http://localhost:3000
```

1つ目のブラウザで次のように入力する。

```text
Name: Alice
Message: Hello
```

`Send` をクリックする。

2つ目のブラウザで次のように入力する。

```text
Name: Bob
Message: Hi Alice
```

`Send` をクリックする。

両方のブラウザに次のように表示されれば成功である。

```text
Alice: Hello
Bob: Hi Alice
```

---

## 8. ミニ課題10の提出内容

ミニ課題10では、**Step 4 の完成版のみ**を提出する。

提出するファイルは次の2つである。

```text
chatapp/server/server.js
chatapp/client/src/App.js
```

提出方法は、Manaba+R の指示に従う。

!!! important
    Step 1、Step 2、Step 3 は提出しなくてよい。

    ただし、Step 4 を理解するための練習として、順番に実装することを推奨する。

---

## 9. よくあるエラーと確認ポイント

### 9.1 `node server.js` が動かない

現在いる場所を確認する。

正しい場所は次である。

```text
chatapp/server/
```

正しいコマンドは次である。

```bash
node server.js
```

もし `chatapp/` にいる場合は、先に次を入力する。

```bash
cd server
```

---

### 9.2 `socket.io-client` が見つからない

React 側で `socket.io-client` がインストールされていない可能性がある。

`chatapp/client` に移動する。

```bash
cd chatapp/client
```

次のコマンドを実行する。

```bash
npm install socket.io-client
```

その後、React を再起動する。

```bash
npm start
```

---

### 9.3 `server.js` を変更したのに反映されない

`server.js` を変更した場合は、サーバーの再起動が必要である。

サーバーのターミナルで次を押す。

```text
Ctrl + C
```

その後、次を実行する。

```bash
node server.js
```

---

### 9.4 ブラウザが自動で開かない

次の URL を手動で開く。

```text
http://localhost:3000
```

---

### 9.5 チャットが2つのブラウザに表示されない

次を確認する。

- サーバーが起動しているか
- Reactクライアントが起動しているか
- 両方のブラウザで `http://localhost:3000` を開いているか
- `server.js` のチャット送信で `io.emit` を使っているか
- `server.js` を変更したあと、サーバーを再起動したか

---

## 10. まとめ

Week 10 では、Socket.IO を使ったリアルタイム通信を学んだ。

| Step | 内容 |
|---|---|
| Step 1 | サーバーから Reactクライアントにメッセージを送る |
| Step 2 | Reactクライアントからサーバーにメッセージを送る |
| Step 3 | 匿名チャットを作成する |
| Step 4 | 名前付きチャットを作成する |

ミニ課題10では、Step 4 の完成版を提出する。
