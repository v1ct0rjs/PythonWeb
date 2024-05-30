/** @jsxImportSource @emotion/react */


import { Fragment, useContext, useEffect, useState } from "react"
import { ColorModeContext, EventLoopContext, StateContexts } from "/utils/context"
import { Event, getBackendURL, isTrue, refs } from "/utils/state"
import { AppWindowIcon as LucideAppWindowIcon, CalculatorIcon as LucideCalculatorIcon, CalendarPlusIcon as LucideCalendarPlusIcon, DicesIcon as LucideDicesIcon, GithubIcon as LucideGithubIcon, InstagramIcon as LucideInstagramIcon, LinkedinIcon as LucideLinkedinIcon, MailIcon as LucideMailIcon, MessageSquareTextIcon as LucideMessageSquareTextIcon, NetworkIcon as LucideNetworkIcon, SendIcon as LucideSendIcon, SignpostBigIcon as LucideSignpostBigIcon, WatchIcon as LucideWatchIcon, WifiOffIcon as LucideWifiOffIcon } from "lucide-react"
import { keyframes } from "@emotion/react"
import { toast, Toaster } from "sonner"
import env from "/env.json"
import { Avatar as RadixThemesAvatar, Box as RadixThemesBox, Button as RadixThemesButton, Flex as RadixThemesFlex, Heading as RadixThemesHeading, Link as RadixThemesLink, Text as RadixThemesText } from "@radix-ui/themes"
import Script from "next/script"
import NextLink from "next/link"
import { FloatButton } from "antd"
import NextHead from "next/head"



export function Link_99ec4e7f524dac1890eef4c13d09f8cb () {



  return (
    <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}, "width": "100%"}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`https://github.com/v1ct0rjs/Pyng`} passHref={true}>
  <RadixThemesButton css={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "0.5em", "color": "#000000", "backgroundColor": "#1dd3b0", "&:hover": {"backgroundColor": "#FFFFFF"}}}>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%", "alignItems": "start"}} direction={`row`} gap={`3`}>
  <RadixThemesBox>
  <LucideNetworkIcon css={{"width": "2em", "height": "2em", "margin": "0.8em", "color": "#000000"}}/>
</RadixThemesBox>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} direction={`column`} gap={`0`}>
  <RadixThemesText as={`p`} css={{"fontSize": "1.5em", "color": "#000000", "fontFamily": "JetBrains Mono"}}>
  {`Pyng`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#086375", "fontFamily": "JetBrains Mono"}}>
  {`Script detector of LAN equipment`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_42f7bd22b75a1143ba1471bade93606a () {



  return (
    <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}, "width": "100%"}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`https://www.instagram.com/dj_10tacle/`} passHref={true}>
  <RadixThemesButton css={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "0.5em", "color": "#000000", "backgroundColor": "#1dd3b0", "&:hover": {"backgroundColor": "#FFFFFF"}}}>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%", "alignItems": "start"}} direction={`row`} gap={`3`}>
  <RadixThemesBox>
  <LucideInstagramIcon css={{"width": "2em", "height": "2em", "margin": "0.8em", "color": "#000000"}}/>
</RadixThemesBox>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} direction={`column`} gap={`0`}>
  <RadixThemesText as={`p`} css={{"fontSize": "1.5em", "color": "#000000", "fontFamily": "JetBrains Mono"}}>
  {`Instagram`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#086375", "fontFamily": "JetBrains Mono"}}>
  {`Instagram Profile`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_496773d6621d4a19167ba9dcd09641ba () {



  return (
    <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`https://reflex.dev/`} passHref={true}>
  <img alt={`Logo de reflex`} css={{"width": "150px", "paddingLeft": "2em"}} src={`/Reflex_white.svg`}/>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_c6b78a03f473c36fec02965992b31cb7 () {



  return (
    <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`https://t.me/p3sc4`} passHref={true}>
  <LucideSendIcon css={{"color": "var(--current-color)"}} size={20}/>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_3c96128c7fc23a15646dbd000cbe8955 () {



  return (
    <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}, "width": "100%"}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`https://github.com/v1ct0rjs/RuletaDeLaFortuna/`} passHref={true}>
  <RadixThemesButton css={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "0.5em", "color": "#000000", "backgroundColor": "#1dd3b0", "&:hover": {"backgroundColor": "#FFFFFF"}}}>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%", "alignItems": "start"}} direction={`row`} gap={`3`}>
  <RadixThemesBox>
  <LucideDicesIcon css={{"width": "2em", "height": "2em", "margin": "0.8em", "color": "#000000"}}/>
</RadixThemesBox>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} direction={`column`} gap={`0`}>
  <RadixThemesText as={`p`} css={{"fontSize": "1.5em", "color": "#000000", "fontFamily": "JetBrains Mono"}}>
  {`Wheel of Fortune`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#086375", "fontFamily": "JetBrains Mono"}}>
  {`Wheel of fortune game`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_c1b7f3cf41fd390a650d0626db360150 () {



  return (
    <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}, "width": "100%"}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`https://github.com/v1ct0rjs/pyther`} passHref={true}>
  <RadixThemesButton css={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "0.5em", "color": "#000000", "backgroundColor": "#1dd3b0", "&:hover": {"backgroundColor": "#FFFFFF"}}}>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%", "alignItems": "start"}} direction={`row`} gap={`3`}>
  <RadixThemesBox>
  <LucideMessageSquareTextIcon css={{"width": "2em", "height": "2em", "margin": "0.8em", "color": "#000000"}}/>
</RadixThemesBox>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} direction={`column`} gap={`0`}>
  <RadixThemesText as={`p`} css={{"fontSize": "1.5em", "color": "#000000", "fontFamily": "JetBrains Mono"}}>
  {`Pyter`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#086375", "fontFamily": "JetBrains Mono"}}>
  {`Small client-server messaging program that uses gprc`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
  )
}

export function Toaster_89416713a273995fc60191a4cf573054 () {
  const [ colorMode, toggleColorMode ] = useContext(ColorModeContext)


  refs['__toast'] = toast
  const [addEvents, connectErrors] = useContext(EventLoopContext);
  
const toast_props = {"description": `Check if server is reachable at ${getBackendURL(env.EVENT).href}`, "closeButton": true, "duration": 120000, "id": "websocket-error"};
const [userDismissed, setUserDismissed] = useState(false);
useEffect(() => {
    if (connectErrors.length >= 2) {
        if (!userDismissed) {
            toast.error(
                `Cannot connect to server: ${(connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : ''}.`,
                {...toast_props, onDismiss: () => setUserDismissed(true)},
            )
        }
    } else {
        toast.dismiss("websocket-error");
        setUserDismissed(false);  // after reconnection reset dismissed state
    }
}, [connectErrors]);

  return (
    <Toaster closeButton={false} expand={true} position={`bottom-right`} richColors={true} theme={colorMode}/>
  )
}

export function Link_669eae52bc55c27e66716f3d7118ee95 () {



  return (
    <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}, "width": "100%"}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`https://github.com/v1ct0rjs/PythonWeb`} passHref={true}>
  <RadixThemesButton css={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "0.5em", "color": "#000000", "backgroundColor": "#1dd3b0", "&:hover": {"backgroundColor": "#FFFFFF"}}}>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%", "alignItems": "start"}} direction={`row`} gap={`3`}>
  <RadixThemesBox>
  <LucideAppWindowIcon css={{"width": "2em", "height": "2em", "margin": "0.8em", "color": "#000000"}}/>
</RadixThemesBox>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} direction={`column`} gap={`0`}>
  <RadixThemesText as={`p`} css={{"fontSize": "1.5em", "color": "#000000", "fontFamily": "JetBrains Mono"}}>
  {`Python Web App`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#086375", "fontFamily": "JetBrains Mono"}}>
  {`Code of this same web programmed in Python`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_6552ff20095c6352173ba6927de4f340 () {



  return (
    <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}, "width": "100%"}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`https://github.com/v1ct0rjs/m5_move-detector`} passHref={true}>
  <RadixThemesButton css={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "0.5em", "color": "#000000", "backgroundColor": "#1dd3b0", "&:hover": {"backgroundColor": "#FFFFFF"}}}>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%", "alignItems": "start"}} direction={`row`} gap={`3`}>
  <RadixThemesBox>
  <LucideWatchIcon css={{"width": "2em", "height": "2em", "margin": "0.8em", "color": "#000000"}}/>
</RadixThemesBox>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} direction={`column`} gap={`0`}>
  <RadixThemesText as={`p`} css={{"fontSize": "1.5em", "color": "#000000", "fontFamily": "JetBrains Mono"}}>
  {`Activity detection bracelet`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#086375", "fontFamily": "JetBrains Mono"}}>
  {`Micropython program to compete in the TELECO GAMES`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_43dc7e1576f15acbe56acf8dcfc46bd3 () {



  return (
    <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}, "width": "100%"}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`https://github.com/v1ct0rjs`} passHref={true}>
  <RadixThemesButton css={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "0.5em", "color": "#000000", "backgroundColor": "#1dd3b0", "&:hover": {"backgroundColor": "#FFFFFF"}}}>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%", "alignItems": "start"}} direction={`row`} gap={`3`}>
  <RadixThemesBox>
  <LucideGithubIcon css={{"width": "2em", "height": "2em", "margin": "0.8em", "color": "#000000"}}/>
</RadixThemesBox>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} direction={`column`} gap={`0`}>
  <RadixThemesText as={`p`} css={{"fontSize": "1.5em", "color": "#000000", "fontFamily": "JetBrains Mono"}}>
  {`GitHub`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#086375", "fontFamily": "JetBrains Mono"}}>
  {`Project repositories`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_a173df9d06ddc5bee952974c2694e72e () {



  return (
    <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`https://www.python.org/`} passHref={true}>
  <img alt={`Logo de Python, dos serpientes entrelazadas`} css={{"width": "100px", "paddingRight": "2em"}} src={`/python.svg`}/>
</NextLink>
</RadixThemesLink>
  )
}

export function Fragment_312722142985dfbd0ef6b8c2e3e9e9e0 () {
  const state__page_state = useContext(StateContexts.state__page_state)



  return (
    <Fragment>
  {isTrue(state__page_state.is_live) ? (
  <Fragment>
  <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`https://www.twitch.tv/dj_10tacle`} passHref={true}>
  <img css={{"color": "#1dd3b0", "width": "4em", "height": "4em", "marginTop": "-10px", "marginRight": "0.8em"}} src={`/twitch.svg`}/>
</NextLink>
</RadixThemesLink>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export function Div_ac2a89ea84667d600a059f034bd91dfe () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <div css={{"position": "fixed", "width": "100vw", "height": "0"}} title={`Connection Error: ${(connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : ''}`}>
  <Fragment_cf53a535ae2e610a113dd361eb6ac95b/>
</div>
  )
}

export function Fragment_cf53a535ae2e610a113dd361eb6ac95b () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <Fragment>
  {isTrue(connectErrors.length > 0) ? (
  <Fragment>
  <LucideWifiOffIcon css={{"color": "crimson", "zIndex": 9999, "position": "fixed", "bottom": "33px", "right": "33px", "animation": `${pulse} 1s infinite`}} size={32}/>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export function Link_cd4fae1f6091b002228585676408552b () {



  return (
    <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}, "width": "100%"}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`https://mastodon.social/@v1ct0rjs`} passHref={true}>
  <RadixThemesButton css={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "0.5em", "color": "#000000", "backgroundColor": "#1dd3b0", "&:hover": {"backgroundColor": "#FFFFFF"}}}>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%", "alignItems": "start"}} direction={`row`} gap={`3`}>
  <RadixThemesBox>
  <img alt={`Icono`} css={{"width": "2em", "height": "2em", "margin": "0.8em"}} src={`/mastodon.svg`}/>
</RadixThemesBox>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} direction={`column`} gap={`0`}>
  <RadixThemesText as={`p`} css={{"fontSize": "1.5em", "color": "#000000", "fontFamily": "JetBrains Mono"}}>
  {`Mastodon`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#086375", "fontFamily": "JetBrains Mono"}}>
  {`Mastodon Profile`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_6b58647510723708d66a534fb8f24817 () {



  return (
    <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}, "width": "100%"}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`https://github.com/v1ct0rjs/PyAgenda`} passHref={true}>
  <RadixThemesButton css={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "0.5em", "color": "#000000", "backgroundColor": "#1dd3b0", "&:hover": {"backgroundColor": "#FFFFFF"}}}>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%", "alignItems": "start"}} direction={`row`} gap={`3`}>
  <RadixThemesBox>
  <LucideCalendarPlusIcon css={{"width": "2em", "height": "2em", "margin": "0.8em", "color": "#000000"}}/>
</RadixThemesBox>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} direction={`column`} gap={`0`}>
  <RadixThemesText as={`p`} css={{"fontSize": "1.5em", "color": "#000000", "fontFamily": "JetBrains Mono"}}>
  {`PyAgenda`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#086375", "fontFamily": "JetBrains Mono"}}>
  {`Script, CLI task manager`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_7c583465a79cf4a89c0d9d8269475078 () {



  return (
    <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}, "width": "100%"}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`https://github.com/v1ct0rjs/DBOH`} passHref={true}>
  <RadixThemesButton css={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "0.5em", "color": "#000000", "backgroundColor": "#1dd3b0", "&:hover": {"backgroundColor": "#FFFFFF"}}}>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%", "alignItems": "start"}} direction={`row`} gap={`3`}>
  <RadixThemesBox>
  <LucideCalculatorIcon css={{"width": "2em", "height": "2em", "margin": "0.8em", "color": "#000000"}}/>
</RadixThemesBox>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} direction={`column`} gap={`0`}>
  <RadixThemesText as={`p`} css={{"fontSize": "1.5em", "color": "#000000", "fontFamily": "JetBrains Mono"}}>
  {`DBOH Converter`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#086375", "fontFamily": "JetBrains Mono"}}>
  {`Decimal, Binary, Hexadecimal and Octal Converter`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
  )
}

const pulse = keyframes`
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
`


export function Link_925f4303694c22801750f2641511b498 () {



  return (
    <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}, "width": "100%"}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`https://www.linkedin.com/in/v%C3%ADctor-manuel-jim%C3%A9nez-s%C3%A1nchez-53286130b/`} passHref={true}>
  <RadixThemesButton css={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "0.5em", "color": "#000000", "backgroundColor": "#1dd3b0", "&:hover": {"backgroundColor": "#FFFFFF"}}}>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%", "alignItems": "start"}} direction={`row`} gap={`3`}>
  <RadixThemesBox>
  <LucideLinkedinIcon css={{"width": "2em", "height": "2em", "margin": "0.8em", "color": "#000000"}}/>
</RadixThemesBox>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} direction={`column`} gap={`0`}>
  <RadixThemesText as={`p`} css={{"fontSize": "1.5em", "color": "#000000", "fontFamily": "JetBrains Mono"}}>
  {`LinkedIn`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#086375", "fontFamily": "JetBrains Mono"}}>
  {`LinkedIn Profile`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_57c13f28e4522652b9138412a74a24c8 () {



  return (
    <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`mailto:vmjimenezs02@educarex.es`} passHref={true}>
  <LucideMailIcon css={{"color": "var(--current-color)"}} size={20}/>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_048836d216a87df48d9e75cc0c013366 () {



  return (
    <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}, "width": "100%"}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`https://github.com/v1ct0rjs/ahorcado/`} passHref={true}>
  <RadixThemesButton css={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "0.5em", "color": "#000000", "backgroundColor": "#1dd3b0", "&:hover": {"backgroundColor": "#FFFFFF"}}}>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%", "alignItems": "start"}} direction={`row`} gap={`3`}>
  <RadixThemesBox>
  <LucideSignpostBigIcon css={{"width": "2em", "height": "2em", "margin": "0.8em", "color": "#000000"}}/>
</RadixThemesBox>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} direction={`column`} gap={`0`}>
  <RadixThemesText as={`p`} css={{"fontSize": "1.5em", "color": "#000000", "fontFamily": "JetBrains Mono"}}>
  {`Hangman`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#086375", "fontFamily": "JetBrains Mono"}}>
  {`Word guessing game`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_33bc1c82d4131b9a817ae39c3eb3eb6d () {



  return (
    <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}, "width": "100%"}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`https://x.com/vmjimsan`} passHref={true}>
  <RadixThemesButton css={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "0.5em", "color": "#000000", "backgroundColor": "#1dd3b0", "&:hover": {"backgroundColor": "#FFFFFF"}}}>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%", "alignItems": "start"}} direction={`row`} gap={`3`}>
  <RadixThemesBox>
  <img alt={`Icono`} css={{"width": "2em", "height": "2em", "margin": "0.8em"}} src={`/x-twitter.svg`}/>
</RadixThemesBox>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} direction={`column`} gap={`0`}>
  <RadixThemesText as={`p`} css={{"fontSize": "1.5em", "color": "#000000", "fontFamily": "JetBrains Mono"}}>
  {`X`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#086375", "fontFamily": "JetBrains Mono"}}>
  {`X Profile`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_5f2591cb00d73926e4c02137cd62a91e () {



  return (
    <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`https://www.kernel.org/`} passHref={true}>
  <img alt={`Logo de Tux, la mascota de Linux un pinguino`} css={{"width": "60px"}} src={`/Tux_Mono.png`}/>
</NextLink>
</RadixThemesLink>
  )
}

export default function Component() {

  return (
    <Fragment>
  <Fragment>
  <Div_ac2a89ea84667d600a059f034bd91dfe/>
  <Toaster_89416713a273995fc60191a4cf573054/>
</Fragment>
  <RadixThemesBox>
  <Script strategy={`afterInteractive`}>
  {`document.documentElement.lang = 'es'`}
</Script>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"position": "sticky", "background": "#000000", "paddingInlineStart": "0.5em", "paddingInlineEnd": "0.5em", "paddingTop": "0.5em", "paddingBottom": "0.5em", "zIndex": "999", "top": "0", "fontFamily": "Ubuntu Sans Mono", "fontWeight": "600"}} direction={`row`} gap={`3`}>
  <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}}}>
  <NextLink href={`/`} passHref={true}>
  <RadixThemesText align={`center`} as={`p`} css={{"color": "#1dd3b0", "fontSize": "1.5em"}}>
  {`['V1cT0r', 'l1nuX3r', 'PyTh0n1st', 'D3v3l0p3r']`}
</RadixThemesText>
</NextLink>
</RadixThemesLink>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"justifyContent": "end", "marginLeft": "auto"}} direction={`row`} gap={`3`}>
  <Fragment_312722142985dfbd0ef6b8c2e3e9e9e0/>
</RadixThemesFlex>
</RadixThemesFlex>
  <RadixThemesFlex css={{"display": "flex", "alignItems": "center", "justifyContent": "center", "widht": "100%", "marginTop": "2em", "marginBottom": "2em"}}>
  <RadixThemesFlex align={`center`} className={`rx-Stack`} css={{"maxWidth": "600px"}} direction={`column`} gap={`6`}>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"alignItems": "start", "fontFamily": "JetBrains Mono"}} direction={`column`} gap={`5`}>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} direction={`row`} gap={`5`}>
  <RadixThemesAvatar css={{"name": "Víctor Jiménez", "borderColor": "#086375", "borderWidth": "3px", "alt": "Avatar de Víctor Jiménez"}} fallback={`VJ`} highContrast={false} radius={`full`} size={`8`} src={`/avatar.png`} variant={`solid`}/>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} direction={`column`} gap={`3`}>
  <RadixThemesHeading css={{"fontSize": "2em", "marginBottom": "-15px", "marginTop": "5px", "color": "#1dd3b0", "fontFamily": "JetBrains Mono", "fontWeight": "700"}}>
  {`Víctor Jiménez`}
</RadixThemesHeading>
  <RadixThemesText as={`p`} css={{"fontSize": "0.8em", "color": "#FFFFFF"}}>
  {`Developer, Pythonist 🐍 and Linuxer 🐧`}
</RadixThemesText>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} direction={`row`} gap={`3`}>
  <RadixThemesFlex>
  <RadixThemesBox css={{"fontSize": "0.8em", "color": "#FFFFFF"}}>
  <RadixThemesText as={`p`} css={{"fontWeight": "bold", "color": "#1dd3b0"}}>
  {`Zafra, Badajoz, Extremadura`}
</RadixThemesText>
  {`Spain 🇪🇸`}
</RadixThemesBox>
</RadixThemesFlex>
</RadixThemesFlex>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"color": "#1dd3b0"}} direction={`row`} gap={`3`}>
  <RadixThemesText as={`p`} css={{"fontSize": "0.8em", "color": "#FFFFFF"}}>
  {`Contact: `}
</RadixThemesText>
  <Link_57c13f28e4522652b9138412a74a24c8/>
  <Link_c6b78a03f473c36fec02965992b31cb7/>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesFlex>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#FFFFFF"}}>
  {`Hello 👋, I am an enthusiastic developer 😊 with a solid knowledge in Python 🐍, HTML 🌐, C 🖥️, electronics 🔌, and servers 💾.
I have programmed for home automation projects 🛠️ and now I am expanding my horizons towards frontend development 🎨.`}
</RadixThemesText>
</RadixThemesFlex>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%"}} direction={`column`} gap={`3`}>
  <RadixThemesHeading css={{"stiles": {"width": "100%", "padding": "0.8em", "color": "#1dd3b0"}, "color": "#1dd3b0", "fontSize": "2em", "fontFamily": "JetBrains Mono", "fontWeight": "700"}}>
  {`Projects`}
</RadixThemesHeading>
  <Link_43dc7e1576f15acbe56acf8dcfc46bd3/>
  <Link_c1b7f3cf41fd390a650d0626db360150/>
  <Link_3c96128c7fc23a15646dbd000cbe8955/>
  <Link_048836d216a87df48d9e75cc0c013366/>
  <Link_6b58647510723708d66a534fb8f24817/>
  <Link_6552ff20095c6352173ba6927de4f340/>
  <Link_99ec4e7f524dac1890eef4c13d09f8cb/>
  <Link_7c583465a79cf4a89c0d9d8269475078/>
  <Link_669eae52bc55c27e66716f3d7118ee95/>
</RadixThemesFlex>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%"}} direction={`column`} gap={`3`}>
  <RadixThemesHeading css={{"stiles": {"width": "100%", "padding": "0.8em", "color": "#1dd3b0"}, "color": "#1dd3b0", "fontSize": "2em", "fontFamily": "JetBrains Mono", "fontWeight": "700"}}>
  {`Certifications`}
</RadixThemesHeading>
  <RadixThemesBox css={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "0.5em", "color": "#000000", "backgroundColor": "#000000", "border": "4px", "borderColor": "#1dd3b0", "borderStyle": "solid"}}>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%", "alignItems": "center"}} direction={`row`} gap={`3`}>
  <img alt={`Sello de certificación Cisco`} css={{"width": "4em", "height": "4em", "margin": "0.8em"}} src={`/cybersecurity-essentials.png`}/>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} direction={`column`} gap={`0`}>
  <RadixThemesText as={`p`} css={{"fontSize": "1.5em", "color": "#1dd3b0", "fontFamily": "JetBrains Mono"}}>
  {`Cybersecurity Cisco`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#086375", "fontFamily": "JetBrains Mono"}}>
  {`Cybersecurity Certificate`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesBox>
</RadixThemesFlex>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%"}} direction={`column`} gap={`3`}>
  <RadixThemesHeading css={{"stiles": {"width": "100%", "padding": "0.8em", "color": "#1dd3b0"}, "color": "#1dd3b0", "fontSize": "2em", "fontFamily": "JetBrains Mono", "fontWeight": "700"}}>
  {`Social Networks`}
</RadixThemesHeading>
  <Link_925f4303694c22801750f2641511b498/>
  <Link_33bc1c82d4131b9a817ae39c3eb3eb6d/>
  <Link_cd4fae1f6091b002228585676408552b/>
  <Link_42f7bd22b75a1143ba1471bade93606a/>
</RadixThemesFlex>
  <FloatButton href={`/`} icon={<img src={`/languages.svg`}/>}/>
</RadixThemesFlex>
</RadixThemesFlex>
  <RadixThemesFlex align={`center`} className={`rx-Stack`} css={{"color": "#086375", "backgroundColor": "#000000", "fontFamily": "JetBrains Mono"}} direction={`column`} gap={`3`}>
  <RadixThemesFlex css={{"display": "flex", "alignItems": "center", "justifyContent": "center"}}>
  <RadixThemesFlex align={`center`} className={`rx-Stack`} direction={`row`} gap={`3`}>
  <Link_a173df9d06ddc5bee952974c2694e72e/>
  <Link_5f2591cb00d73926e4c02137cd62a91e/>
  <Link_496773d6621d4a19167ba9dcd09641ba/>
</RadixThemesFlex>
</RadixThemesFlex>
  <RadixThemesText as={`p`} css={{"fontSize": "1em"}}>
  {`2023 - 2024 By Víctor Jiménez V1.3`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesBox>
  <NextHead>
  <title>
  {`V1cT0r's Portfolio`}
</title>
  <meta content={`Hello 👋, I am an enthusiastic developer 😊 with a solid knowledge in Python 🐍, HTML 🌐, C 🖥️, electronics 🔌, and servers 💾.
I have programmed for home automation projects 🛠️ and now I am expanding my horizons towards frontend development 🎨.`} name={`description`}/>
  <meta content={`/avatar.png`} property={`og:image`}/>
  <meta content={`V1cT0r's Portfolio`} name={`og:title`}/>
  <meta content={`Hello 👋, I am an enthusiastic developer 😊 with a solid knowledge in Python 🐍, HTML 🌐, C 🖥️, electronics 🔌, and servers 💾.
I have programmed for home automation projects 🛠️ and now I am expanding my horizons towards frontend development 🎨.`} name={`og:description`}/>
  <meta content={`website`} name={`og:type`}/>
  <meta content={`/preview.png`} name={`og:image`}/>
  <meta content={`summary_large_image`} name={`twitter:card`}/>
  <meta content={`@vmjimsan`} name={`twitter:site`}/>
</NextHead>
</Fragment>
  )
}
