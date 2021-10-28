// const fs = require('fs');
// let [NSP, ...connections] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let NSP = '21 6 12';
let connections = [
  '1 9',
  '1 10',
  '10 12',
  '2 13',
  '13 11',
  '11 12',
  '3 8',
  '8 7',
  '8 12',
  '5 19',
  '5 14',
  '14 12',
  '6 20',
  '6 21',
  '20 15',
  '15 12',
  '4 18',
  '4 17',
  '17 16',
  '16 12'
];
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}
class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }
  enQueue(value) {
    let node = new Node(value);
    if (this.head == null) {
      this.head = node;
      this.head.next = this.tail;
    }
    else this.tail.next = node;
    this.tail = node;
    this.size++;
  }
  deQueue() {
    let ret = this.head;
    this.head = this.head.next;
    this.size--;
    return ret;
  }
  getSize() {
    return this.size;
  }
}
let [N, S, P] = NSP.split(' ').map(Number);
let link = Array(N + 1).fill().map(e => []);
connections.map(el => {
  let [s, e] = el.split(' ').map(Number);
  link[s].push(e);
  link[e].push(s);
});
let answer = 0;
let life = 2;
let queue = new Queue();
queue.enQueue([P, 0, -1]); // 현위치, 카운트, 전위치
while (queue.getSize() > 0) {
  let [curr, cnt, prev] = queue.deQueue().value;
  if (curr <= S) {
    answer += cnt;
    life--;
    if (life <= 0) break;
  }
  else {
    let next = link[curr];
    next.map(e => {
      if (e != prev) {
        queue.enQueue([e, cnt + 1, curr]);
      }
    });
  }
}
console.log(N - answer - 1)