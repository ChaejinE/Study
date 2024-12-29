export function makeImagePath(id: string, format : string = "original") {
    console.log(format, id);
    return `https://image.tmdb.org/t/p/${format}/${id}`;
}
