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

export const App = () => {
  const { data: algorithmsData, isLoading } = useGetAlgorithms();
  const {
    mutate: mutateEncode,
    data: encodeData,
    isPending: isPendingEncode,
    reset: resetEncode,
  } = usePostEncode();
  const {
    mutate: mutateDecode,
    data: decodeData,
    isPending: isPendingDecode,
    reset: resetDecode,
  } = usePostDecode();
  const [algorithm, setAlgorithm] = useState("");
  const [encodingMessage, setEncodingMessage] = useState("");
  const [decodingMessage, setDecodingMessage] = useState("");

  useEffect(() => {
    if (algorithmsData.length === 1) setAlgorithm(algorithmsData[0].key);
  }, [algorithmsData]);

  const handleChangeAlgorithm = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setAlgorithm(event.target.value);
    setEncodingMessage("");
    setDecodingMessage("");
    resetEncode();
    resetDecode();
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

  const handleClickEncode = () => {
    mutateEncode({
      algorithm,
      word: encodingMessage,
    });
  };

  const handleClickDecode = () => {
    mutateDecode({
      algorithm,
      codeword: decodingMessage.split(" "),
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
              {algorithmsData.map((algorithm) => (
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
      {!!encodeData?.codeword?.length && (
        <Styles.WrapperResult>
          {encodeData?.codeword.map((word) => word).join(" ")}
        </Styles.WrapperResult>
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
      {!!decodeData?.word && (
        <Styles.WrapperResult>{decodeData.word}</Styles.WrapperResult>
      )}
    </Styles.Wrapper>
  );
};
