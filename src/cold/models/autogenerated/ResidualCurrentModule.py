
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricCurrentModule import ElectricCurrent



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class ResidualCurrent(ElectricCurrent, ElectrochemicalQuantity):
    """
    Class representing the `ResidualCurrent` entity, which inherits from:
    - ElectricCurrent, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_07e219c3_890f_488f_bd96_bee8e445d764'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ResidualCurrent'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ResidualCurrent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_07e219c3_890f_488f_bd96_bee8e445d764',
    
    class_name='ResidualCurrent',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_07e219c3_890f_488f_bd96_bee8e445d764',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ResidualCurrent',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    