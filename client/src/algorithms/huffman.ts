type TFreq = {
  [key: string]: number;
};

type TCodes = { [key: string]: string };

type TNode = [TNode, TNode] | [string, number];

const getNodeFreq = (node: TNode): number => {
  return Array.isArray(node[0])
    ? getNodeFreq(node[0]) + getNodeFreq(node[1] as TNode)
    : (node[1] as number);
};

const buildHuffmanTree = (freq: TFreq): TNode => {
  const nodes: TNode[] = Object.entries(freq).map(([char, freq]) => [
    char,
    freq,
  ]);

  while (nodes.length > 1) {
    nodes.sort((a, b) => getNodeFreq(a) - getNodeFreq(b));

    const left = nodes.shift()!;
    const right = nodes.shift()!;

    const newNode: TNode = [left, right];

    nodes.push(newNode);
  }

  return nodes[0];
};

const generateHuffmanCodes = (node: TNode, prefix: string = ""): TCodes => {
  let codes: TCodes = {};

  const traverse = (currentNode: TNode, currentCode: string) => {
    if (typeof currentNode[0] === "string") {
      codes[currentNode[0]] = currentCode;
    } else {
      traverse(currentNode[0], currentCode + "0");
      traverse(currentNode[1] as TNode, currentCode + "1");
    }
  };

  traverse(node, prefix);
  return codes;
};

export const encodeHuffman = (word: string) => {
  const freq: TFreq = {};

  for (const char of word) {
    if (freq[char]) {
      freq[char]++;
    } else {
      freq[char] = 1;
    }
  }

  const huffmanTree = buildHuffmanTree(freq);

  const huffmanCodes = generateHuffmanCodes(huffmanTree);

  let encodedString = "";
  for (const char of word) {
    encodedString += huffmanCodes[char];
  }

  return { encoded: encodedString, tree: JSON.stringify(huffmanTree) };
};

export const decodeHuffman = (encoded: string, tree: string): string => {
  const jsonTree = JSON.parse(tree);
  let decodedString = "";
  let currentNode: TNode = jsonTree;

  for (const bit of encoded) {
    if (bit === "0") {
      currentNode = currentNode[0] as TNode;
    } else {
      currentNode = currentNode[1] as TNode;
    }

    if (typeof currentNode[0] === "string") {
      decodedString += currentNode[0];
      currentNode = jsonTree;
    }
  }

  return decodedString;
};
