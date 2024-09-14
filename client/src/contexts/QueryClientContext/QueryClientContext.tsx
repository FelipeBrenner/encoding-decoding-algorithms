import {
	QueryClient,
	QueryClientProvider as TanstackQueryClientProvider,
} from "@tanstack/react-query";
import type { PropsWithChildren } from "react";

const client = new QueryClient({
	defaultOptions: {
		queries: {
			refetchOnWindowFocus: false,
			refetchOnMount: false,
			refetchOnReconnect: false,
			retry: false,
		},
	},
});

export const QueryClientProvider = ({ children }: PropsWithChildren) => {
	return (
		<TanstackQueryClientProvider client={client}>
			{children}
		</TanstackQueryClientProvider>
	);
};
