# Workflow for Claude-sessions

Dette repoet er en personlig arbeidsbok for ett bryllup. Én bruker, ingen
review-prosess. Workflowen skal være **så enkel som mulig** – konflikter
oppstår når parallelle sessions endrer samme fil uten å være i sync.

## Regel 1: Sync med main FØR du gjør endringer

Ved starten av hver session, kjør:

```bash
git fetch origin
git rebase origin/main
```

Hvis sessionen startet på en feature-branch (`claude/...`), rebase den
mot `origin/main` først. Hvis det er konflikt der, løs den med en gang
før du begynner på selve oppgaven.

## Regel 2: Push til main når du er ferdig

Når oppgaven er ferdig:

```bash
git checkout main
git pull origin main
git merge <feature-branch> --no-ff
git push origin main
```

Ingen PR-er nødvendig – brukeren er eneste eier og vil ha alt på main
direkte. Slett gjerne feature-branchen lokalt etterpå.

**Unntak**: Hvis brukeren eksplisitt ber om en PR, lag PR mot `main` på
vanlig måte.

## Regel 3: Ved konflikt – varsle brukeren

Hvis merge mot main gir konflikt som ikke er triviell (mer enn whitespace
eller åpenbare flettinger), stopp og vis brukeren konflikten før du
løser den. Brukeren har som regel kontekst om hvilken versjon som skal
vinne.

## Hvorfor dette

Tidligere har parallelle sessions opprettet feature-branches som har
divergert mye fra main, som har gitt store konflikter. Sync-først-flyten
holder alle branches nær main og gjør konflikter små og håndterbare.
