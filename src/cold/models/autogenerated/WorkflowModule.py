
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ProcedureModule import Procedure





from .RoleModule import Role



from .TaskModule import Task





class Workflow(Procedure):
    """
    Class representing the `Workflow` entity, which inherits from:
    - Procedure

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_64963ed6_39c9_4258_85e0_6466c4b5420c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Workflow'`
        - **Alias**: `class_name`
    
    - `hasHolisticPart` (`Optional[Role]`): 
        - **Default Value**: `None`
        - **Alias**: `hasHolisticPart`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasTask` (`Optional[Task]`): 
        - **Default Value**: `None`
        - **Alias**: `hasTask`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Workflow(
    
    class_iri='https://w3id.org/emmo#EMMO_64963ed6_39c9_4258_85e0_6466c4b5420c',
    
    class_name='Workflow',
    
    hasHolisticPart="example_value",
    
    elucidation="example_value",
    
    hasTask=None,
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_64963ed6_39c9_4258_85e0_6466c4b5420c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Workflow',
        alias="class_name"
    )
    
    hasHolisticPart: Optional[Role] = Field(
        None,
        alias="hasHolisticPart"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    hasTask: Optional[Task] = Field(
        None,
        alias="hasTask"
    )
    

    
    @validator("hasHolisticPart", pre=True, always=True)
    def validate_hasHolisticPart(cls, value):
        if value is not None and not isinstance(value, Role):
            raise ValueError(f"Field 'hasHolisticPart' must be an instance of 'Role' or its subclass.")
        return value
    
    @validator("hasTask", pre=True, always=True)
    def validate_hasTask(cls, value):
        if value is not None and not isinstance(value, Task):
            raise ValueError(f"Field 'hasTask' must be an instance of 'Task' or its subclass.")
        return value
    
    

    

    