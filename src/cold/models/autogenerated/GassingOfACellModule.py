
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalPhenomenonModule import ElectrochemicalPhenomenon







class GassingOfACell(ElectrochemicalPhenomenon):
    """
    Class representing the `GassingOfACell` entity, which inherits from:
    - ElectrochemicalPhenomenon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0f827b54_370d_4c63_99a6_80f13b24e55e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GassingOfACell'`
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
    obj = GassingOfACell(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0f827b54_370d_4c63_99a6_80f13b24e55e',
    
    class_name='GassingOfACell',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0f827b54_370d_4c63_99a6_80f13b24e55e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GassingOfACell',
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
    

    
    

    

    