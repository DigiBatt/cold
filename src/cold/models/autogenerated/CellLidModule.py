
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalConstituentModule import ElectrochemicalConstituent







class CellLid(ElectrochemicalConstituent):
    """
    Class representing the `CellLid` entity, which inherits from:
    - ElectrochemicalConstituent

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1e33e37e_d7c9_4701_ba6d_a09456a13aaf'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CellLid'`
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
    obj = CellLid(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1e33e37e_d7c9_4701_ba6d_a09456a13aaf',
    
    class_name='CellLid',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1e33e37e_d7c9_4701_ba6d_a09456a13aaf',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CellLid',
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
    

    
    

    

    