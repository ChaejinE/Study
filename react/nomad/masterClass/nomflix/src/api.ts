const API_KEY = "13f4e316ddda9abc861cbcdb9a2446af"
const BASE_PATH = "https://api.themoviedb.org/3"

export function getMovies() {
    return fetch(`${BASE_PATH}/movie/now_playing?api_key=${API_KEY}`)
        .then((response) => response.json());  
}
