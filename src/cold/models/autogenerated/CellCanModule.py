
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalConstituentModule import ElectrochemicalConstituent







class CellCan(ElectrochemicalConstituent):
    """
    Class representing the `CellCan` entity, which inherits from:
    - ElectrochemicalConstituent

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4a5660bd_1c1a_40e5_8a41_463c720d3903'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CellCan'`
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
    obj = CellCan(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4a5660bd_1c1a_40e5_8a41_463c720d3903',
    
    class_name='CellCan',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4a5660bd_1c1a_40e5_8a41_463c720d3903',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CellCan',
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
    

    
    

    

    