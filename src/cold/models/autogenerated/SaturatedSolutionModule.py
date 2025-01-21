
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SolutionModule import Solution







class SaturatedSolution(Solution):
    """
    Class representing the `SaturatedSolution` entity, which inherits from:
    - Solution

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_27a81a51_e8d7_42fb_834f_0d068fa45d89'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SaturatedSolution'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SaturatedSolution(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_27a81a51_e8d7_42fb_834f_0d068fa45d89',
    
    class_name='SaturatedSolution',
    
    IEVReference="example_value",
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_27a81a51_e8d7_42fb_834f_0d068fa45d89',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SaturatedSolution',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    