
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DensityModule import Density



from .ChemicalCompositionQuantityModule import ChemicalCompositionQuantity



from .ConcentrationModule import Concentration







class MassConcentration(Density, ChemicalCompositionQuantity, Concentration):
    """
    Class representing the `MassConcentration` entity, which inherits from:
    - Density, ChemicalCompositionQuantity, Concentration

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_16f2fe60_2db7_43ca_8fee_5b3e416bfe87'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MassConcentration'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MassConcentration(
    
    class_iri='https://w3id.org/emmo#EMMO_16f2fe60_2db7_43ca_8fee_5b3e416bfe87',
    
    class_name='MassConcentration',
    
    iupacReference="example_value",
    
    qudtReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_16f2fe60_2db7_43ca_8fee_5b3e416bfe87',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MassConcentration',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    

    
    

    

    