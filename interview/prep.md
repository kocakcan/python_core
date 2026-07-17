# Python Interview Prep Plan — Junior Data Engineer (Round 2)

**Interview:** Monday, 45 minutes, 3 panelists
- Liubov Fedorovich — Project Coordinator (likely process/culture fit, lower technical depth)
- Artemy Dmitriev — Lead Developer (asks "how does it work under the hood" — memory, internals, string formatting, generics)
- Anton — Team Lead (likely engineering judgment, trade-offs, possibly architecture/design)

**Round 1 recap:** Background/project discussion + string formatting internals question (f-strings vs .format() memory). No live coding occurred. Round 2 will likely skip intro and go straight into deeper technical territory. Coding exercise possible but likely short/verbal rather than a full algorithm challenge.

---

## Tier 1 — High Priority (Artemy's pattern: internals/"how it works")

- [x] **String interning** — CPython caches literals/small ints (-5 to 256), `is` vs `==`, why dynamically built strings (f-strings, `.format()`) aren't interned
- [x] **f-strings vs `.format()` vs `%`** — memory behavior, eager evaluation, performance, logging gotcha (`%` is lazy in logging calls)
- [x] **Memory management** — reference counting (`sys.getrefcount`), `id()`, garbage collection for circular references (`gc.collect()`)
- [x] **Mutable vs immutable types** — mutable default argument bug (`def f(x=[])`) and the fix
- [x] **Shallow vs deep copy** — `copy.copy()` vs `copy.deepcopy()`, shared references in nested structures
- [x] **Generators & iterators** — `yield`, laziness, `StopIteration`, memory efficiency vs lists, infinite generators
  - Practiced: `chunked()`, `filter_gen()`, `take()`, `pairwise()`, composed pipeline (filter → chunk)
- [x] **Decorators** — `@decorator` = `func = decorator(func)`, `functools.wraps`, decorator factories (args), timing decorator exercise
- [x] **Context managers** — `with` statement, `__enter__`/`__exit__`, `contextlib.contextmanager`
- [ ] **GIL** — why it exists, threading vs multiprocessing for CPU-bound vs I/O-bound tasks

## Tier 2 — Likely (Anton: engineering judgment)

- [ ] **OOP fundamentals** — classes, inheritance, `@classmethod` vs `@staticmethod`, magic methods (`__repr__`, `__eq__`)
- [ ] **SOLID principles** — covered conceptually (S/O/L/I/D with examples); have a real project story ready (Congress Summary / auth work)
- [ ] **Exception handling best practices** — custom exceptions, try/except/finally patterns for data pipelines
- [ ] **Testing basics** — `pytest` fundamentals, mocking
- [ ] **Data structures & complexity** — list/dict/set/tuple trade-offs, Big-O of common operations

## Tier 3 — Possible, Lower Priority

- [ ] **Async/await basics**
- [ ] **Type hints / Generics** — `TypeVar`, `Generic`, PEP 695 syntax (already covered, solid)
- [ ] **Design patterns** — only if Anton steers toward architecture

---

## Data Engineer Domain Topics (secondary track, if time allows)

- [ ] **Pandas essentials** — reading CSV/JSON/SQL, filtering, groupby, merge/join, NaN handling, `apply()` vs vectorized ops
- [ ] **Basic SQL** — joins, group by, aggregates, window functions
- [ ] **datetime/timezones** — common pain points
- [ ] **ETL/ELT concepts** — one-liner definitions, batch vs streaming, idempotency, data validation

---

## IoC / Dependency Injection / FastAPI Depends() (already covered, reference only)
- IoC = principle ("don't call us, we'll call you" / Hollywood Principle)
- DI = implementation technique of IoC; relates directly to **Dependency Inversion Principle (SOLID - D)**
- FastAPI `Depends()` — function/class/yield dependencies, caching per request, `dependency_overrides` for testing

---

## Study Schedule
- **Thu/Fri:** Finish Tier 1 (decorators, context managers, GIL)
- **Sat:** Tier 2 (OOP, exceptions, testing, data structures) + 1-2 mock coding drills
- **Sun:** Light review only, no new material — recap Tier 1 + Tier 2 highlights
- **Sun night:** Prepare 2-3 questions to ask the panel; review your own project talking points (Congress Summary, Cognito/auth work)

---

## Reminders / Meta Tips
- If unsure of an answer, **say so honestly and reason out loud** (worked well in Round 1 — Artemy responded positively to this)
- Narrate thought process during any coding — communication is weighted heavily in short interviews
- Have **2-3 questions ready for the panel** at the end
- Tie technical answers back to real project experience where possible (e.g., SOLID → auth service structure, generators → potential data pipeline work)