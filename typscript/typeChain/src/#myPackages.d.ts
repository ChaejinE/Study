interface Config {
    urls: string
}

declare module "myPackages" {
    function init(config: Config): boolean;
    function exit(code: number): number;
}
