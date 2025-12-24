import Description from "@/components/Description";
import Image from "next/image";
import SectionDivider from "@/components/SectionDivider";
export default function Home() {
  return (
   <main className="flex-col items-center text-center">
    <Description/>
    <SectionDivider/>
   </main>
  );
}
