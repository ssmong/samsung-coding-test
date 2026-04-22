---
trigger: 함수에 리스트/딕셔너리 넘겼는데 바깥에서도 바뀌는지 헷갈릴 때, 또는 반대로 수정했는데 안 바뀔 때
related_problems: [14499, 3190]
---

# 파이썬 변경 가능 객체(mutable) 참조 전달

## 언제 쓰나
- 함수에 리스트/딕셔너리 넘겨서 **안에서 수정**할 때 — 반환 필요한지 판단
- 같은 보드를 여러 함수가 건드리는 시뮬레이션
- `visited`, `board`, `dice`, `snake` 등 공유 상태 다룰 때
- 스냅샷 필요한지 (`deepcopy`) 판단할 때

## 핵심 규칙
파이썬 인자 전달은 **"객체 참조의 값 복사(pass-by-object-reference)"**.

| 타입 | 함수 안에서 수정 가능? | 바깥에 반영됨? |
|---|---|---|
| `list`, `dict`, `set`, 사용자 객체 | ✅ in-place 가능 | ✅ 반영됨 |
| `int`, `str`, `tuple`, `frozenset` | ❌ 불가 (불변) | — |

**구분점은 "이름 재할당"과 "내용 수정"이 다르다는 것.**

```python
def modify(lst):
    lst[0] = 99       # ✅ 내용 수정 → 바깥에 반영
    lst.append(4)     # ✅ 내용 수정 → 바깥에 반영

def reassign(lst):
    lst = [9, 9, 9]   # ❌ 이름 재할당 → 바깥과 연결 끊김

a = [1, 2, 3]
modify(a);   print(a)   # [99, 2, 3, 4]
reassign(a); print(a)   # [99, 2, 3, 4]  (변화 없음)
```

## 코드 — 주사위/보드 패턴
```python
def roll(dice, d):
    t, b, n, s, e, w = dice
    # 인덱스 대입 = in-place 수정 → 바깥 dice도 바뀜
    dice[0], dice[4], dice[1], dice[5] = w, t, e, b
# 반환 불필요. 호출은 그냥 roll(dice, d)
```

vs. 새 리스트를 만드는 경우:
```python
def rotated(dice, d):
    return [w, b, n, s, t, dice[5]]   # 새 리스트
dice = rotated(dice, d)                # 받아야 함
```

## 함정
- **`=` 대입은 수정이 아니라 재바인딩.** `lst = [...]` (함수 안) = 원본 안 바뀜.
- **슬라이스 대입은 in-place.** `lst[:] = [...]`는 내용 교체라서 바깥 반영됨. 전체 교체할 땐 이 관용구 유용.
- **얕은 복사 주의.** `new = old.copy()`나 `new = old[:]`는 2D 격자에서 행이 공유됨. 2D는 `copy.deepcopy(old)` 또는 `[row[:] for row in old]`.
- **동시 수정 버그.** 여러 객체가 같은 리스트를 가리키는데 한쪽에서 수정하면 다른 쪽도 바뀜. 시뮬레이션에서 "이번 턴 상태"와 "다음 턴 상태"를 같은 보드에 쓰면 꼬임 → 스냅샷 필요.
- **기본 인자 함정.** `def f(x, memo=[]):`의 `memo`는 호출 간 공유됨. 기본값으로 mutable 쓰지 말 것.

## 판별 체크리스트
함수 작성 전 자문:
1. 이 함수가 인자를 **수정**하나, **읽기만** 하나?
2. 수정한다면 **같은 객체를 바꾸나** (반환 불필요), **새 객체를 만드나** (반환 필요)?
3. 호출자가 원본을 보존해야 하나? → 함수 진입 시 `arr[:]` 또는 `deepcopy`로 복사.

## 관련 개념
- [00-data-structures.md](00-data-structures.md) — mutable/immutable 타입 분류
