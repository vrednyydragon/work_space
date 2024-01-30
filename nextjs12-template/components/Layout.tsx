import Navbar from "./Navbar";
import Head from "next/head";
import React, {ReactNode} from 'react';


type Props = {
    children: ReactNode,
    title: string,
}


const Layout = ({children, title = 'Custom App',}: Props): JSX.Element => {

    return (
        <>
            <Head>
                <title>{title}</title>
            </Head>
            <Navbar/>
            <main>
                {children}
            </main>
        </>
    )
}

export default Layout
