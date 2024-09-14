import { Theme, createTheme as muiCreateTheme } from "@mui/material";
import { baseThemeOptions } from "./base-theme-options";
import { darkThemeOptions } from "./dark-theme-options";

export const createTheme = (): Theme => {
  const theme = muiCreateTheme(baseThemeOptions, darkThemeOptions);

  return theme;
};
