import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { CssBaseline, ThemeProvider } from "@mui/material";
import { createTheme } from "@themes";
import { QueryClientProvider } from "@contexts";
import { App } from "App";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <ThemeProvider theme={createTheme()}>
      <CssBaseline />
      <QueryClientProvider>
        <App />
      </QueryClientProvider>
    </ThemeProvider>
  </StrictMode>
);
