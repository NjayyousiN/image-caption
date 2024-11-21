import "./globals.css";
import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Image Captioning",
  description: "Image-to-text application",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
      >
        {children}
      </body>
    </html>
  );
}
