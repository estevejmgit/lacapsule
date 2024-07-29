import React from "react";
import { Container, Typography } from "@material-ui/core";

import CypressLogo from "../components/SvgCypressLogo";
import LaCapsuleLogo from "../components/SvgLaCapsuleLogo";

export default function Footer() {
  return (
    <Container
      maxWidth="sm"
      style={{ marginTop: 50, display: "flex", flexDirection: "column", marginTop: "-30" }}
    >
      <Typography variant="body2" color="textSecondary" align="center">
        End-to-end tested with
        <a
          style={{ textDecoration: "none" }}
          target="_blank"
          rel="noopener noreferrer"
          href="https://lacapsule.academy"
        >
          <CypressLogo
            style={{
              marginTop: -2,
              marginLeft: 5,
              height: "20px",
              width: "55px",
              verticalAlign: "middle",
            }}
          />
        </a>
      </Typography>
      <Typography variant="body2" color="textSecondary" align="center">
        <a
          style={{ textDecoration: "none" }}
          target="_blank"
          rel="noopener noreferrer"
          href="https://lacapsule.academy"
        >
          <LaCapsuleLogo
            style={{
              marginLeft: 5,
              width: "30px",
              verticalAlign: "bottom",
            }}
          />
        </a>
      </Typography>
    </Container>
  );
}
