import { useMutation } from "@tanstack/react-query";
import axios from "axios";

interface IPostEncodeVariables {
  algorithm: string;
  word: string;
}

interface IPostEncodeResponse {
  codeword: Array<string>;
}

export const usePostEncode = () => {
  const { mutate, data, isPending } = useMutation<
    IPostEncodeResponse,
    Error,
    IPostEncodeVariables
  >({
    mutationFn: async (data) => {
      const response = await axios.post("http://127.0.0.1:8080/encode", data);
      return response.data;
    },
  });

  return { mutate, data, isPending };
};
