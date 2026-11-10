export default function HomePage() {
  return (
    <main className="shell">
      <nav className="nav" aria-label="Main navigation">
        <a className="brand" href="/">PoultryLink</a>
        <span className="tag">Early product foundation</span>
      </nav>
      <section className="hero">
        <p className="eyebrow">A connected poultry value chain</p>
        <h1>Find poultry products.<br />Connect with the right people.</h1>
        <p className="intro">
          PoultryLink is being built to connect farmers, buyers, suppliers and
          service providers through clearer listings and structured demand.
        </p>
        <div className="actions">
          <a className="primary" href="https://github.com/zulyadainimuhammad/poultrylink">Explore the project</a>
        </div>
        <p className="notice">Product preview only — marketplace transactions are not yet enabled.</p>
      </section>
      <section className="pillars" aria-label="Product direction">
        <article><h2>Discover supply</h2><p>Explore structured listings for birds, eggs, chicks, feed and poultry inputs.</p></article>
        <article><h2>Share demand</h2><p>Publish buyer requests with quantity, location, timing and product requirements.</p></article>
        <article><h2>Understand markets</h2><p>Build towards reliable market information using structured, traceable data.</p></article>
      </section>
      <footer>© {new Date().getFullYear()} PoultryLink. Building a more connected poultry market.</footer>
    </main>
  );
}
