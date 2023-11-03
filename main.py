import fastapi
from pydantic import BaseModel
from typing import List, Dict, Any


issues = [
    {'id': 1, 'name': 'do something 1', 'deadline': '01.01.2024'},
    {'id': 2, 'name': 'do something 2', 'deadline': '02.02.2024'},
    {'id': 3, 'name': 'do something 3', 'deadline': '03.03.2024'},
]

router = fastapi.APIRouter(prefix='/api')


@router.get('/issues')
def get_issues() -> List[Dict]:
    return issues


@router.get('/issues/{issue_id}')
def get_issue(issue_id: int) -> List[Dict]:
    return [issue for issue in issues if issue.get('id') == issue_id]


class Issue(BaseModel):
    id: int
    name: str
    deadline: str


@router.post('/issues/add')
def add_issue(issue: List[Issue]) -> List[Any]:
    issues.extend(issue)
    return issues


@router.post('/issues/{issue_id}')
def edit_issue(issue_id: int, new_name: str) -> Dict[str, Any]:
    issue = [issue for issue in issues if issue.get('id') == issue_id][0]
    issue['name'] = new_name
    return issue


app = fastapi.FastAPI(
    title='Issue Tracker'
)
app.include_router(router)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', reload=True)
