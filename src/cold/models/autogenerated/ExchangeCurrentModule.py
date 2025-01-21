
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricCurrentModule import ElectricCurrent



from .ElectrochemicalKineticQuantityModule import ElectrochemicalKineticQuantity







class ExchangeCurrent(ElectricCurrent, ElectrochemicalKineticQuantity):
    """
    Class representing the `ExchangeCurrent` entity, which inherits from:
    - ElectricCurrent, ElectrochemicalKineticQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ccde24bb_790a_40ca_a06e_cea156a61031'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ExchangeCurrent'`
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
    obj = ExchangeCurrent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ccde24bb_790a_40ca_a06e_cea156a61031',
    
    class_name='ExchangeCurrent',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ccde24bb_790a_40ca_a06e_cea156a61031',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ExchangeCurrent',
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
    

    
    

    

    