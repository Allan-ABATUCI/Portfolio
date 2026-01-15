import Description from "@/components/Description";
import SectionDivider from "@/components/SectionDivider";
import Projects from "@/components/Projects";
export default function Home() {
  return (
   <main className=" flex flex-col items-center text-center">
    <Description/>
    <SectionDivider/>
    <Projects/>
   </main>
  );
}
