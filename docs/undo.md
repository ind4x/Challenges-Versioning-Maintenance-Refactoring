# Reversal strategies in Git

Bottom Line Up Front: This guide details the technical differences between
`git restore` and `git reset` for managing changes in a repository.
Understanding these operations is critical for maintaining repository
integrity and managing local development states.

## Comparison of operations

### 1. Git restore
*   **Scope**: Modifies the working directory only.
*   **Function**: Discards uncommitted local changes to return a file to the
    state of the last commit.
*   **Impact**: Safe for use in shared branches as it does not alter commit
    history.

### 2. Git reset
*   **Scope**: Modifies the repository history.
*   **Function**: Moves the branch pointer (HEAD) to a specified previous
    commit.
*   **Impact**: Can potentially erase recent history; requires caution when
    working with remote branches.

## Technical application

1.  Use `git restore <file>` when you need to undo uncommitted changes in a
    specific file.
2.  Use `git reset --hard <commit>` when you need to revert the entire project
    to a known stable state in the past.

Authored by Youssef Fellah.
Developed for the Engineering Cycle - Mundiapolis University.
