// import original module declarations
import 'styled-components';


// and extend them!
// https://styled-components.com/docs/api#typescript
declare module 'styled-components' {
  export interface DefaultTheme {
    textColor: string;
    bgColor: string;
    btnColor: string;
  }
}
