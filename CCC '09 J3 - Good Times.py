ottawa = int(input())
hours = ottawa // 100
minutes = ottawa % 100

victoria_hours = hours - 3
if victoria_hours < 0:
    victoria_hours += 24
victoria = victoria_hours*100 + minutes

edmonton_hours = hours - 2
if edmonton_hours < 0:
    edmonton_hours += 24
edmonton = edmonton_hours*100 + minutes

winnipeg_hours = hours - 1
if winnipeg_hours < 0:
    winnipeg_hours += 24
winnipeg = winnipeg_hours*100 + minutes

halifax_hours = hours +1
if halifax_hours < 0:
    halifax_hours += 24
halifax = halifax_hours*100 + minutes

st_johns_hours = hours + 1
st_johns_minutes = minutes + 30
if st_johns_minutes >= 60:
    st_johns_hours += 1
    st_johns_minutes -= 60
if st_johns_hours >= 24:
    st_johns_hours -= 24
st_johns = st_johns_hours * 100 + st_johns_minutes

print(f'{str(ottawa)} in Ottawa')
print(f'{str(victoria)} in Victoria')
print(f'{str(edmonton)} in Edmonton')
print(f'{str(winnipeg)} in Winnipeg')
print(f'{str(ottawa)} in Toronto')
print(f'{str(halifax)} in Halifax')
print(f"{str(st_johns)} in St. John's")



