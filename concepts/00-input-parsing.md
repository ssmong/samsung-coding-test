---
trigger: 백준 문제 입력을 파싱할 때. 특히 혼합 타입(int + char) 줄이 있을 때.
related_problems: [3190]
---

# 입력 파싱 관용구

## 언제 쓰나

모든 백준 풀이의 첫 단계. sys.stdin 최적화와 타입 변환 패턴은 거의 고정이다.

## 코드

```python
import sys
input = sys.stdin.readline   # 반드시. input() 그대로는 느림.

# 1. 단일 정수
N = int(input())

# 2. 여러 정수 한 줄 → 고정 개수 변수
R, C = map(int, input().split())

# 3. 여러 정수 한 줄 → 리스트
arr = list(map(int, input().split()))

# 4. 혼합 타입 (int + char) — split은 모두 str을 주므로 개별 변환
x, c = input().split()
x = int(x)
# c는 그대로 'L' / 'D' 등

# 5. 여러 줄을 한 번에 (엄청 빠름, 줄 수가 많을 때)
data = sys.stdin.read().split()
idx = 0
N = int(data[idx]); idx += 1
# ...
```

## 함정

- **`input()` 그대로 쓰면 느리다.** `sys.stdin.readline`으로 재정의하는 게 백준 관용구. 재정의 안 하고 그대로 `sys.stdin.readline()`을 호출하면 개행 문자가 붙어서 `int()`엔 문제 없지만 문자열 비교(`c == 'L'`)는 `'L\n'` 때문에 실패할 수 있음 → **혼합 타입일 땐 `.split()` 해야 안전**.
- **`input().split()`은 항상 `list[str]`**이다. 한 개만 정수여도 `map(int, ...)` 뭉텅이로 변환 못 함. `x, c = input().split(); x = int(x)` 패턴으로 쪼개라.
- **`map(int, ...)` vs 리스트 컴프리헨션** — 둘 다 OK지만 map이 약간 더 빠르고 짧다. 백준 관용구는 map.
- **`list.pop(0)`은 O(N)**이다. 입력 자체에서 나오는 실수는 아니지만, 파싱 후 소비 패턴으로 쓰면 TLE. 소비 순서가 있다면 `deque.popleft()` 또는 인덱스 변수.
- **대량 입력**(N ≥ 10^5 줄)은 `sys.stdin.read().split()` 일괄 읽기가 훨씬 빠르다. 일반 시뮬레이션은 readline으로 충분.

## 관련 개념

- [01-grid-template.md](01-grid-template.md) — 격자 문제 기본 세팅
- [../templates/io.py](../templates/io.py) — I/O 템플릿 전체
