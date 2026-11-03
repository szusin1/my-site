import { ComingSoon } from "@/components/ComingSoon";
import { loadLatest } from "@/lib/reasoning-store";
import { TwoWayTable } from "@/components/reasoning/TwoWayTable";
import { BernoulliFourViews } from "@/components/reasoning/BernoulliFourViews";

export const metadata = { title: "Reasoning & Uncertainty Service" };

// Freshness contract: without this line, Next.js may serve a cached copy of
// this page, and the grader would see stale numbers seconds after your API
// answered. force-dynamic re-renders the page on every request.
export const dynamic = "force-dynamic";

export default async function ReasoningPage() {
  const { syllogism, plausibility, bernoulli } = await loadLatest();

  // Until the first probe arrives, keep the honest placeholder.
  if (!syllogism && !plausibility && !bernoulli) {
    return (
      <ComingSoon
        lane={2}
        title="Reasoning & Uncertainty"
        description="A service that audits syllogisms, updates beliefs on base rates, and reads Bernoulli businesses. Built after Lane 2."
      />
    );
  }

  return (
    <main className="mx-auto max-w-3xl px-6 py-14">
      <p className="text-sm font-semibold uppercase tracking-[0.2em] text-accent">
        Lane 2 · live decision service
      </p>
      <h1 className="mt-3 text-4xl font-bold">My Reasoning &amp; Uncertainty Service</h1>
      {/* TODO(yours): My service helps make sense of uncertainty by checking reasoning, probabilities, and expected outcomes. */}
      <p className="mt-4 max-w-prose text-muted">
        Below is the most recent problem my API solved, for each of the three problem types it
        speaks. Every number on this page comes from the same live data my API answered with.
      </p>

      <section className="mt-12">
        <h2 className="text-2xl font-bold">Latest syllogism audit</h2>
        {syllogism ? (
          <div className="mt-3 max-w-prose">
            <p className="text-muted">
              Rule: if {String(syllogism.problem.rule?.if)}, then{" "}
              {String(syllogism.problem.rule?.then)}.
            </p>
            <p className="mt-1 text-muted">
              {String(syllogism.problem.observation?.statement)}{" "}
              {String(syllogism.problem.conclusion?.statement)}
            </p>
            <p className="mt-3 text-lg">
              Verdict:{" "}
              <strong data-reasoning="verdict" className="text-accent">
                {String(syllogism.answer.verdict)}
              </strong>
              {typeof syllogism.answer.fallacy === "string" && (
                <span className="text-muted"> ({syllogism.answer.fallacy})</span>
              )}
            </p>
            {/* TODO(yours): The service looks at the structure of an argument rather than the situation being described. It checks if the conclusion follows the rule, instead of assuming something is true just because it sounds reasonable. */}
            <p className="mt-2 max-w-prose text-sm text-muted">
              How the service decided: it ignores the story and reads only the shape of
              the argument. The rule promises that the if-part brings the then-part, so
              only two observations prove anything: the if-part being true, or the
              then-part being false. Every other shape proves nothing, no matter how
              believable the story feels.
            </p>
          </div>
        ) : (
          <p className="mt-3 text-muted">No syllogism probe yet.</p>
        )}
      </section>

      <section className="mt-12">
        <h2 className="text-2xl font-bold">Latest plausibility update</h2>
        {plausibility ? (
          <div className="mt-3">
            <p className="text-xs font-semibold uppercase tracking-widest text-muted">
              The problem, exactly as the grader sent it
            </p>
            <p className="mt-1 max-w-prose text-muted">{String(plausibility.problem.scenario)}</p>
            <TwoWayTable
              baseRate={Number(plausibility.problem.baseRate)}
              hitRate={Number(plausibility.problem.hitRate)}
              falseAlarmRate={Number(plausibility.problem.falseAlarmRate)}
            />
            <p className="mt-3 text-lg">
              Posterior:{" "}
              <strong data-reasoning="posterior" className="text-accent">
                {Number(plausibility.answer.posterior).toFixed(3)}
              </strong>
            </p>
            {/* TODO(yours): This percentage tells a manager how likely a flagged case is to be a true positive, helping them decide whether further investigation is necessary. */}
          </div>
        ) : (
          <p className="mt-3 text-muted">No plausibility probe yet.</p>
        )}
      </section>

      <section className="mt-12">
        <h2 className="text-2xl font-bold">Latest Bernoulli read: four views</h2>
        {bernoulli ? (
          <div className="mt-3">
            <p className="text-xs font-semibold uppercase tracking-widest text-muted">
              The problem, exactly as the grader sent it
            </p>
            <p className="mt-1 max-w-prose text-muted">{String(bernoulli.problem.scenario)}</p>
            <BernoulliFourViews
              theta={Number(bernoulli.problem.theta)}
              onSuccess={Number(bernoulli.problem.payoffs?.onSuccess)}
              onFailure={Number(bernoulli.problem.payoffs?.onFailure)}
            />
            <p className="mt-4 text-lg">
              Expected payoff:{" "}
              <strong data-reasoning="expected-value" className="text-accent">
                {Number(bernoulli.answer.expectedValue).toFixed(2)}
              </strong>
              <span className="ml-3 text-base text-muted">
                P(X = {String(bernoulli.problem.probabilityOf)}) ={" "}
                {Number(bernoulli.answer.probabilityStatement).toFixed(2)}
              </span>
            </p>
            {/* TODO(yours): Expected payoff helps estimate the average return over time, but an individual result could be higher or lower depending on whether the event succeeds or fails. */}
          </div>
        ) : (
          <p className="mt-3 text-muted">No Bernoulli probe yet.</p>
        )}
      </section>
    </main>
  );
}