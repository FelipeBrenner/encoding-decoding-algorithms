import { useEffect, useState } from "react";
import * as Styles from "./App.styles";
import {
  CircularProgress,
  FormControl,
  FormControlLabel,
  FormLabel,
  Radio,
  RadioGroup,
  TextField,
} from "@mui/material";
import { LoadingButton } from "@mui/lab";
import { useGetAlgorithms, usePostDecode, usePostEncode } from "@api";
import { decodeHuffman, encodeHuffman } from "@algorithms";

export const App = () => {
  const { data: algorithmsData, isLoading } = useGetAlgorithms();
  const {
    mutate: mutateEncode,
    data: encodeData,
    isPending: isPendingEncode,
  } = usePostEncode();
  const {
    mutate: mutateDecode,
    data: decodeData,
    isPending: isPendingDecode,
  } = usePostDecode();
  const [algorithm, setAlgorithm] = useState("");
  const [encodingMessage, setEncodingMessage] = useState("");
  const [decodingMessage, setDecodingMessage] = useState("");
  const [golombK, setGolombK] = useState("");
  const [huffmanEncodedTree, setHuffmanEncodedTree] = useState("");
  const [huffmanDecodingTree, setHuffmanDecodingTree] = useState("");
  const [huffmanEncoded, setHuffmanEncoded] = useState("");
  const [huffmanDecoded, setHuffmanDecoded] = useState("");

  useEffect(() => {
    if (algorithmsData.length === 1) setAlgorithm(algorithmsData[0].key);
  }, [algorithmsData]);

  const handleChangeAlgorithm = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setAlgorithm(event.target.value);
  };

  const handleChangeEncodingMessage = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setEncodingMessage(event.target.value);
  };

  const handleChangeDecodingMessage = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setDecodingMessage(event.target.value);
  };

 const handleChangeGolombK = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    const value = event.target.value;
    if (/^\d*$/.test(value)) {
      setGolombK(value);
    }
  };

  const handleChangeHuffmanDecodingTree = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setHuffmanDecodingTree(event.target.value);
  };

  const handleClickEncode = () => {
    if (algorithm === "huffman") {
      const { encoded, tree } = encodeHuffman(encodingMessage);
      setHuffmanEncoded(encoded);
      setHuffmanEncodedTree(tree);
      return;
    }

    mutateEncode({
      algorithm,
      word: encodingMessage,
      k: parseInt(golombK, 10)
    });
  };

  const handleClickDecode = () => {
    if (algorithm === "huffman") {
      const decoded = decodeHuffman(decodingMessage, huffmanDecodingTree);
      setHuffmanDecoded(decoded);
      return;
    }

    mutateDecode({
      algorithm,
      codeword: decodingMessage,
      k: parseInt(golombK, 10)
    });
  };

  return (
    <Styles.Wrapper>
      <FormControl>
        <FormLabel>Selecione o algoritmo</FormLabel>
        <Styles.WrapperAlgorithms>
          {isLoading ? (
            <CircularProgress size={16} />
          ) : (
            <RadioGroup row value={algorithm} onChange={handleChangeAlgorithm}>
              {[
                ...algorithmsData,
                {
                  key: "huffman",
                  name: "Huffman",
                },
              ].map((algorithm) => (
                <FormControlLabel
                  key={algorithm.key}
                  value={algorithm.key}
                  label={algorithm.name}
                  control={<Radio />}
                />
              ))}
            </RadioGroup>
          )}
        </Styles.WrapperAlgorithms>
      </FormControl>
      <Styles.WrapperMessage>
        <TextField
          fullWidth
          label="Mensagem para codificar"
          value={encodingMessage}
          onChange={handleChangeEncodingMessage}
        />
        <LoadingButton
          onClick={handleClickEncode}
          loading={isPendingEncode}
          style={{
            width: 110,
          }}
        >
          Codificar
        </LoadingButton>
      </Styles.WrapperMessage>
      {algorithm === "huffman" && huffmanEncoded ? (
        <>
          <Styles.WrapperResult>{huffmanEncoded}</Styles.WrapperResult>
          <Styles.WrapperResult>{huffmanEncodedTree}</Styles.WrapperResult>
        </>
      ) : (
        !!encodeData?.codeword?.length && (
          <Styles.WrapperResult>
            {encodeData?.codeword}
          </Styles.WrapperResult>
        )
      )}
      <Styles.WrapperMessage>
        <TextField
          fullWidth
          label="Mensagem para decodificar"
          value={decodingMessage}
          onChange={handleChangeDecodingMessage}
        />
        <LoadingButton
          onClick={handleClickDecode}
          loading={isPendingDecode}
          style={{
            width: 110,
          }}
        >
          Decodificar
        </LoadingButton>
      </Styles.WrapperMessage>

      {algorithm === "golomb" && (
        <Styles.WrapperMessage>
          <TextField
            fullWidth
            label="Valor de K para Golomb"
            value={golombK}
            onChange={handleChangeGolombK}

          />
        </Styles.WrapperMessage>
      )}
      {algorithm === "huffman" && (
        <TextField
          fullWidth
          label="Árvore para ser utilizada na decodificação do algoritmo Huffman"
          value={huffmanDecodingTree}
          onChange={handleChangeHuffmanDecodingTree}
        />
      )}
      {algorithm === "huffman" && huffmanDecoded ? (
        <Styles.WrapperResult>{huffmanDecoded}</Styles.WrapperResult>
      ) : (
        !!decodeData?.word && (
          <Styles.WrapperResult>{decodeData.word}</Styles.WrapperResult>
        )
      )}
    </Styles.Wrapper>
  );
};
