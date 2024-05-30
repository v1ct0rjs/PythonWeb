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



export function Link_496773d6621d4a19167ba9dcd09641ba () {



  return (
    <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`https://reflex.dev/`} passHref={true}>
  <img alt={`Logo de reflex`} css={{"width": "150px", "paddingLeft": "2em"}} src={`/Reflex_white.svg`}/>
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


export function Link_772629f05d9d913f9c155a0961897754 () {



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
  {`Conversor DBOH`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#086375", "fontFamily": "JetBrains Mono"}}>
  {`Conversor Decimal, Binario, Hexadecimal y Octal`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_578391965dfcae26f49d28248432d06b () {



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
  {`Pulsera detector de actividad`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#086375", "fontFamily": "JetBrains Mono"}}>
  {`Programa en micropython para competir en los TELECO GAMES`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
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

export function Div_ac2a89ea84667d600a059f034bd91dfe () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <div css={{"position": "fixed", "width": "100vw", "height": "0"}} title={`Connection Error: ${(connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : ''}`}>
  <Fragment_cf53a535ae2e610a113dd361eb6ac95b/>
</div>
  )
}

export function Link_b144d8ebaf47cd31dc2c415b56d32b5f () {



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
  {`Ruleta de la fortuna`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#086375", "fontFamily": "JetBrains Mono"}}>
  {`Juego de la ruleta de la fortuna`}
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

export function Link_010b2051dd44ee8e46902658b98e7215 () {



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
  {`Repositorios proyectos`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_1818ba7e5845132cf6a1d6ad124a67d0 () {



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
  {`Pequeño programa de mensajeria cliente-servidor que usa gprc`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_a53a80083926c2cd513842069579601a () {



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
  {`Ahorcado`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#086375", "fontFamily": "JetBrains Mono"}}>
  {`Juego de adivinar palabras`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_679646143fd9774622a1ba053f4bc392 () {



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
  {`Script, gestor de tareas CLI`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_25b1b47921ef664ea3824bd8354d7fd5 () {



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
  {`Perfil De Instagram`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_f7b3566a63f30e7fed7fbd3852609c9b () {



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
  {`Script detector de equipos en LAN`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_21e95c96e633bc98f3fe0a94cf5a0945 () {



  return (
    <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}, "width": "100%"}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`https://x.com/vmjimsan`} passHref={true}>
  <RadixThemesButton css={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "0.5em", "color": "#000000", "backgroundColor": "#1dd3b0", "&:hover": {"backgroundColor": "#FFFFFF"}}}>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%", "alignItems": "start"}} direction={`row`} gap={`3`}>
  <RadixThemesBox>
  <img alt={`Icono`} css={{"width": "2em", "height": "2em", "margin": "0.8em"}} src={`x-twitter.svg`}/>
</RadixThemesBox>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} direction={`column`} gap={`0`}>
  <RadixThemesText as={`p`} css={{"fontSize": "1.5em", "color": "#000000", "fontFamily": "JetBrains Mono"}}>
  {`X`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#086375", "fontFamily": "JetBrains Mono"}}>
  {`Perfil de X`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_cdca847d0ebf4baa8ef46525bdaaa04f () {



  return (
    <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}, "width": "100%"}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`https://mastodon.social/@v1ct0rjs`} passHref={true}>
  <RadixThemesButton css={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "0.5em", "color": "#000000", "backgroundColor": "#1dd3b0", "&:hover": {"backgroundColor": "#FFFFFF"}}}>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%", "alignItems": "start"}} direction={`row`} gap={`3`}>
  <RadixThemesBox>
  <img alt={`Icono`} css={{"width": "2em", "height": "2em", "margin": "0.8em"}} src={`mastodon.svg`}/>
</RadixThemesBox>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} direction={`column`} gap={`0`}>
  <RadixThemesText as={`p`} css={{"fontSize": "1.5em", "color": "#000000", "fontFamily": "JetBrains Mono"}}>
  {`Mastodon`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#086375", "fontFamily": "JetBrains Mono"}}>
  {`Perfil de Mastodon`}
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

export function Link_57c13f28e4522652b9138412a74a24c8 () {



  return (
    <RadixThemesLink asChild={true} css={{"textDecoration": "none", "color": "inherit", "&:hover": {"color": "var(--accent-8)"}}} target={isTrue(true) ? `_blank` : ``}>
  <NextLink href={`mailto:vmjimenezs02@educarex.es`} passHref={true}>
  <LucideMailIcon css={{"color": "var(--current-color)"}} size={20}/>
</NextLink>
</RadixThemesLink>
  )
}

export function Link_7d3c2e44ed7a09849b10248283ea7ca0 () {



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
  {`Código de está web misma web programáda en Python`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
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

export function Link_c8a73496544fd011d1f1c95b736c3f74 () {



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
  {`Perfil De LinkedIn`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesButton>
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
  {`['V1cT0r', 'l1nuX3r0', 'PyTh0n1sta', 'D3v3l0p3r']`}
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
  {`Desarrollador, Pythonista 🐍 y Linuxero 🐧`}
</RadixThemesText>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} direction={`row`} gap={`3`}>
  <RadixThemesFlex>
  <RadixThemesBox css={{"fontSize": "0.8em", "color": "#FFFFFF"}}>
  <RadixThemesText as={`p`} css={{"fontWeight": "bold", "color": "#1dd3b0"}}>
  {`Zafra, Badajoz, Extremadura`}
</RadixThemesText>
  {`España 🇪🇸`}
</RadixThemesBox>
</RadixThemesFlex>
</RadixThemesFlex>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"color": "#1dd3b0"}} direction={`row`} gap={`3`}>
  <RadixThemesText as={`p`} css={{"fontSize": "0.8em", "color": "#FFFFFF"}}>
  {`Contacto: `}
</RadixThemesText>
  <Link_57c13f28e4522652b9138412a74a24c8/>
  <Link_c6b78a03f473c36fec02965992b31cb7/>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesFlex>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#FFFFFF"}}>
  {`Hola 👋, soy un desarrollador entusiasta 😊 con un sólido conocimiento en Python 🐍, HTML 🌐, C 🖥️, electrónica 🔌 y servidores 💾.
He programado para proyectos de domótica 🛠️ y ahora estoy expandiendo mis horizontes hacia el desarrollo frontend 🎨.`}
</RadixThemesText>
</RadixThemesFlex>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%"}} direction={`column`} gap={`3`}>
  <RadixThemesHeading css={{"stiles": {"width": "100%", "padding": "0.8em", "color": "#1dd3b0"}, "color": "#1dd3b0", "fontSize": "2em", "fontFamily": "JetBrains Mono", "fontWeight": "700"}}>
  {`Mis Proyectos`}
</RadixThemesHeading>
  <Link_010b2051dd44ee8e46902658b98e7215/>
  <Link_1818ba7e5845132cf6a1d6ad124a67d0/>
  <Link_b144d8ebaf47cd31dc2c415b56d32b5f/>
  <Link_a53a80083926c2cd513842069579601a/>
  <Link_679646143fd9774622a1ba053f4bc392/>
  <Link_578391965dfcae26f49d28248432d06b/>
  <Link_f7b3566a63f30e7fed7fbd3852609c9b/>
  <Link_772629f05d9d913f9c155a0961897754/>
  <Link_7d3c2e44ed7a09849b10248283ea7ca0/>
</RadixThemesFlex>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%"}} direction={`column`} gap={`3`}>
  <RadixThemesHeading css={{"stiles": {"width": "100%", "padding": "0.8em", "color": "#1dd3b0"}, "color": "#1dd3b0", "fontSize": "2em", "fontFamily": "JetBrains Mono", "fontWeight": "700"}}>
  {`Certificaciones`}
</RadixThemesHeading>
  <RadixThemesBox css={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "0.5em", "color": "#000000", "backgroundColor": "#000000", "border": "4px", "borderColor": "#1dd3b0", "borderStyle": "solid"}}>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%", "alignItems": "center"}} direction={`row`} gap={`3`}>
  <img alt={`Sello de certificación Cisco`} css={{"width": "4em", "height": "4em", "margin": "0.8em"}} src={`/cybersecurity-essentials.png`}/>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} direction={`column`} gap={`0`}>
  <RadixThemesText as={`p`} css={{"fontSize": "1.5em", "color": "#1dd3b0", "fontFamily": "JetBrains Mono"}}>
  {`Cybersecurity Cisco`}
</RadixThemesText>
  <RadixThemesText as={`p`} css={{"fontSize": "1em", "color": "#086375", "fontFamily": "JetBrains Mono"}}>
  {`Certificado de ciberseguridad`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesBox>
</RadixThemesFlex>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"width": "100%"}} direction={`column`} gap={`3`}>
  <RadixThemesHeading css={{"stiles": {"width": "100%", "padding": "0.8em", "color": "#1dd3b0"}, "color": "#1dd3b0", "fontSize": "2em", "fontFamily": "JetBrains Mono", "fontWeight": "700"}}>
  {`Redes Sociales`}
</RadixThemesHeading>
  <Link_c8a73496544fd011d1f1c95b736c3f74/>
  <Link_21e95c96e633bc98f3fe0a94cf5a0945/>
  <Link_cdca847d0ebf4baa8ef46525bdaaa04f/>
  <Link_25b1b47921ef664ea3824bd8354d7fd5/>
</RadixThemesFlex>
  <FloatButton href={`/eng`} icon={<img src={`/languages.svg`}/>}/>
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
  <meta content={`Hola 👋, soy un desarrollador entusiasta 😊 con un sólido conocimiento en Python 🐍, HTML 🌐, C 🖥️, electrónica 🔌 y servidores 💾.
He programado para proyectos de domótica 🛠️ y ahora estoy expandiendo mis horizontes hacia el desarrollo frontend 🎨.`} name={`description`}/>
  <meta content={`/avatar.png`} property={`og:image`}/>
  <meta content={`V1cT0r's Portfolio`} name={`og:title`}/>
  <meta content={`Hola 👋, soy un desarrollador entusiasta 😊 con un sólido conocimiento en Python 🐍, HTML 🌐, C 🖥️, electrónica 🔌 y servidores 💾.
He programado para proyectos de domótica 🛠️ y ahora estoy expandiendo mis horizontes hacia el desarrollo frontend 🎨.`} name={`og:description`}/>
  <meta content={`website`} name={`og:type`}/>
  <meta content={`/preview.png`} name={`og:image`}/>
  <meta content={`summary_large_image`} name={`twitter:card`}/>
  <meta content={`@vmjimsan`} name={`twitter:site`}/>
</NextHead>
</Fragment>
  )
}
