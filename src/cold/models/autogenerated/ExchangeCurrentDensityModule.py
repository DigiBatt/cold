
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricCurrentDensityModule import ElectricCurrentDensity



from .ElectrochemicalKineticQuantityModule import ElectrochemicalKineticQuantity







class ExchangeCurrentDensity(ElectricCurrentDensity, ElectrochemicalKineticQuantity):
    """
    Class representing the `ExchangeCurrentDensity` entity, which inherits from:
    - ElectricCurrentDensity, ElectrochemicalKineticQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e9fd9ef9_adfe_46cb_b2f9_4558468a25e7'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ExchangeCurrentDensity'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ExchangeCurrentDensity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e9fd9ef9_adfe_46cb_b2f9_4558468a25e7',
    
    class_name='ExchangeCurrentDensity',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e9fd9ef9_adfe_46cb_b2f9_4558468a25e7',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ExchangeCurrentDensity',
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
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    