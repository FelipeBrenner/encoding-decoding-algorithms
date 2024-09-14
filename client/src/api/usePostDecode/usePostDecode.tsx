import { useMutation } from "@tanstack/react-query";
import axios from "axios";

interface IPostDecodeVariables {
  algorithm: string;
  codeword: Array<string>;
}

interface IPostDecodeResponse {
  word: string;
}

export const usePostDecode = () => {
  const { mutate, data, isPending } = useMutation<
    IPostDecodeResponse,
    Error,
    IPostDecodeVariables
  >({
    mutationFn: async (data) => {
      const response = await axios.post("http://127.0.0.1:8080/decode", data);
      return response.data;
    },
  });

  return { mutate, data, isPending };
};
