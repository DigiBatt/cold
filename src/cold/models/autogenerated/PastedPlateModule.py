
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CoatedElectrodeModule import CoatedElectrode







class PastedPlate(CoatedElectrode):
    """
    Class representing the `PastedPlate` entity, which inherits from:
    - CoatedElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a1ec9e3c_c624_4848_af13_89a6bc54d77c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PastedPlate'`
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
    obj = PastedPlate(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a1ec9e3c_c624_4848_af13_89a6bc54d77c',
    
    class_name='PastedPlate',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a1ec9e3c_c624_4848_af13_89a6bc54d77c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PastedPlate',
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
    

    
    

    

    