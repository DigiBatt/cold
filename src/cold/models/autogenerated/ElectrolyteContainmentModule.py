
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalPropertyModule import ElectrochemicalProperty







class ElectrolyteContainment(ElectrochemicalProperty):
    """
    Class representing the `ElectrolyteContainment` entity, which inherits from:
    - ElectrochemicalProperty

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_83928dce_9746_4452_a9f9_da4366a20ca4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrolyteContainment'`
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
    obj = ElectrolyteContainment(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_83928dce_9746_4452_a9f9_da4366a20ca4',
    
    class_name='ElectrolyteContainment',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_83928dce_9746_4452_a9f9_da4366a20ca4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrolyteContainment',
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
    

    
    

    

    