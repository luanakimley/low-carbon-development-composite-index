const http = require("http");
const fs = require("fs");

const server = http.createServer((req, res) => {
  fs.readFile("lcdi/lcdi_index.csv", (err, data) => {
    if (err) {
      res.writeHead(404, { "Content-Type": "text/plain" });
      res.end("File not found");
    } else {
      res.writeHead(200, {
        "Content-Type": "text/csv",
        "Access-Control-Allow-Origin": "*",
      });
      res.end(data);
    }
  });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
