docker run --rm -p 5173:5173 -w /usr/src/app -v .:/usr/src/app \
    node:22 \
    npm i && npm run dev
