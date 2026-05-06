---
trigger: 빈도 세기, "가장 많이 나온 K개", 아나그램 판정 등 카운팅이 필요할 때. 또는 Counter가 받는 타입/돌려주는 타입이 헷갈릴 때.
related_problems: []
---

# collections.Counter

## 언제 쓰나
- 여러 종류 원소의 **빈도**가 동시에 필요할 때
- 빈도 정렬 결과 (`most_common(K)`)
- 두 컬렉션의 빈도 차/합 (`c1 + c2`, `c1 - c2`)
- 아나그램 판정 (`Counter(s1) == Counter(s2)`)

**안 쓰는 게 좋은 경우:** 단일 값 카운트만 필요할 땐 `list.count(x)` / `deque.count(x)`가 더 빠르고 간결.

## 받는 자료형 (입력)
**해시 가능한 원소를 담은 모든 iterable.**

```python
Counter([1, 2, 2])           # 리스트 ✓
Counter("aabbc")             # 문자열 ✓ (각 문자별)
Counter((1, 2, 2))           # 튜플 ✓
Counter({'a': 3, 'b': 2})    # dict ✓ (값을 카운트로)
Counter(a=3, b=2)            # 키워드 ✓
Counter(map(tuple, points))  # 좌표는 튜플로 변환 후 ✓
```

❌ list/dict/set은 원소로 못 들어감 (unhashable):
```python
Counter([[1,2], [1,2]])  # TypeError
Counter([(1,2), (1,2)])  # OK → 튜플로 변환
```

## 돌려주는 타입 (반환)
**Counter 자체는 dict 서브클래스** — dict처럼 사용 가능.

| 호출 | 반환 타입 | 예 |
|---|---|---|
| `Counter([...])` | `Counter` | `Counter({'a': 2})` |
| `c[key]` | `int` (없으면 0) | `2` |
| `c.items()` | `dict_items` | `[('a', 2), ('b', 1)]` |
| `c.most_common()` | **`list[tuple]`** | `[('a', 2), ('b', 1)]` |
| `c.most_common(K)` | `list[tuple]` (K개) | `[('a', 2)]` |
| `c.elements()` | iterator (풀어서) | `'a','a','b'` |
| `c + c2` / `c - c2` | `Counter` | 빈도 합/차 |

핵심: `most_common()`만 정렬된 **튜플 리스트**, 나머진 dict 인터페이스.

## 코드
```python
from collections import Counter

c = Counter("abracadabra")
c['a']                  # 5
c['z']                  # 0 (KeyError 안 남)
c.most_common(2)        # [('a', 5), ('b', 2)]
top, n = c.most_common(1)[0]   # 가장 많이 나온 (원소, 빈도) 언패킹

# 빈도 누적
c.update("aaa")         # 기존 카운트에 +
c.subtract("a")         # -

# 두 Counter 연산
Counter("aab") + Counter("abc")  # Counter({'a': 3, 'b': 2, 'c': 1})
Counter("aab") - Counter("a")    # Counter({'a': 1, 'b': 1})  음수는 잘림
```

## 함정
- **빈 Counter는 `Counter()`** (빈 dict와 헷갈리지 말기)
- `c[없는키]`는 0 반환 — 하지만 단순 조회 후 `c['x'] += 1`은 키를 자동 생성. 일반 dict와 다른 점.
- `c - c2`는 **음수를 0으로 자름** (잠재적 함정). 진짜 음수가 필요하면 직접 dict로.
- 원소가 unhashable이면 즉시 TypeError. 격자 좌표는 항상 `tuple`로.
- **시간 복잡도:** 생성 O(N), `most_common(K)` O(N log K). N이 크면 매번 새로 만드는 비용 무시 못 함 → 증감 추적 패턴 고려.

## 단일 카운트엔 Counter 쓰지 말 것
```python
# 느림
Counter(belt)[0] >= K

# 더 간단/빠름
belt.count(0) >= K

# 가장 빠름 (변할 때마다 증감)
broken = 0
if belt[i] == 0:
    broken += 1
```

## 관련 개념
- [00-data-structures.md](00-data-structures.md) — dict/set 등 비교
