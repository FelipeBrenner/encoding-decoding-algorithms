import { Box, Card, Container, styled } from "@mui/material";

export const Wrapper = styled(Container)(({ theme }) => ({
  display: "flex",
  flexDirection: "column",
  gap: theme.spacing(2),
  padding: theme.spacing(3),
  alignItems: "center",
  justifyContent: "center",
  height: "100vh",
}));

export const WrapperAlgorithms = styled(Box)(() => ({
  display: "flex",
  height: 42,
  alignItems: "center",
  justifyContent: "center",
}));

export const WrapperMessage = styled(Box)(({ theme }) => ({
  display: "flex",
  gap: theme.spacing(2),
  width: "100%",
}));

export const WrapperResult = styled(Card)(({ theme }) => ({
  padding: theme.spacing(2),
}));
