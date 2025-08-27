for META in {1..4}
  META=$META envsubst < meta-X.md > meta-${META}.md

