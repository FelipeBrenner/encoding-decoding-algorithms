import { useQuery } from "@tanstack/react-query";
import axios from "axios";

interface IGetAlgorithmsResponse {
  algorithms: {
    key: string;
    name: string;
  }[];
}

export const useGetAlgorithms = () => {
  const { data, isLoading } = useQuery<IGetAlgorithmsResponse>({
    queryKey: ["algorithms"],
    queryFn: async () => {
      const response = await axios.get("http://127.0.0.1:8080/algorithms");
      return response.data;
    },
  });

  return { data: data?.algorithms ?? [], isLoading };
};
