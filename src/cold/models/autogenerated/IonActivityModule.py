
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ActivityOfSoluteModule import ActivityOfSolute







class IonActivity(ActivityOfSolute):
    """
    Class representing the `IonActivity` entity, which inherits from:
    - ActivityOfSolute

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_12b2ec1e_fb89_468a_a51d_97c2a6db297c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IonActivity'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IonActivity(
    
    class_iri='https://w3id.org/emmo#EMMO_12b2ec1e_fb89_468a_a51d_97c2a6db297c',
    
    class_name='IonActivity',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_12b2ec1e_fb89_468a_a51d_97c2a6db297c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IonActivity',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    